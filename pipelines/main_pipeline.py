import os
import time

from edqp.cloud.s3_client import S3Client
from edqp.config.config_loader import ConfigLoader
from edqp.ingestion.ingestion_engine import IngestionEngine
from edqp.logging.logger import PipelineLogger
from edqp.metadata.metadata_writer import MetadataWriter
from edqp.metadata.pipeline_metadata import PipelineMetadata
from edqp.processing.data_separator import DataSeparator
from edqp.registry.rule_registry import RuleRegistry
from edqp.reporting.report_renderer import ReportRenderer
from edqp.reporting.validation_report import ValidationReport
from edqp.storage.dataset_writer import DatasetWriter
from edqp.tracking.pipeline_tracker import PipelineTracker
from edqp.validation.validation_engine import ValidationEngine


class MainPipeline:

    def run(self):

        logger = PipelineLogger().get_logger()

        start = time.perf_counter()

        config = ConfigLoader().get()

        bucket = config["aws"]["bucket"]
        source_file = config["datasets"]["source_file"]

        tracker = PipelineTracker()

        if tracker.is_processed(source_file):

            logger.warning(
                f"{source_file} has already been processed. Skipping pipeline."
            )
            return

        raw_folder = config["paths"]["raw"]
        silver_folder = config["paths"]["silver"]
        quarantine_folder = config["paths"]["quarantine"]
        metadata_folder = config["paths"]["metadata"]

        local_raw_file = os.path.join(raw_folder, source_file)

        local_silver_file = os.path.join(
            silver_folder,
            source_file.replace(".csv", ".parquet"),
        )

        local_quarantine_file = os.path.join(
            quarantine_folder,
            source_file.replace(".csv", ".parquet"),
        )

        local_metadata_file = os.path.join(
            metadata_folder,
            "pipeline_runs.parquet",
        )

        s3 = S3Client()

        s3.download_file(
            bucket=bucket,
            object_name=f"raw/{source_file}",
            local_file=local_raw_file,
        )

        ingestion = IngestionEngine()

        df = ingestion.read(local_raw_file)

        engine = ValidationEngine()

        RuleRegistry().register(
            engine,
            config["validation"],
        )

        validation_results = engine.run(df)

        report = ValidationReport().generate(
            dataset_name=source_file,
            df=df,
            validation_results=validation_results,
        )

        ReportRenderer().display(report)

        valid_df, invalid_df = DataSeparator().split(
            df=df,
            failed_ids=report["failed_ids"],
            primary_key=config["validation"]["primary_key"],
        )

        writer = DatasetWriter()

        writer.save_parquet(
            valid_df,
            local_silver_file,
        )

        writer.save_parquet(
            invalid_df,
            local_quarantine_file,
        )

        execution_time = time.perf_counter() - start

        metadata = PipelineMetadata().create(
            report,
            execution_time,
        )

        MetadataWriter().save(
            metadata,
            local_metadata_file,
        )

        s3.upload_file(
            local_silver_file,
            bucket,
            f"silver/{os.path.basename(local_silver_file)}",
        )

        s3.upload_file(
            local_quarantine_file,
            bucket,
            f"quarantine/{os.path.basename(local_quarantine_file)}",
        )

        s3.upload_file(
            local_metadata_file,
            bucket,
            "metadata/pipeline_runs.parquet",
        )

        tracker.mark_processed(source_file)

        logger.success("Pipeline completed successfully.")