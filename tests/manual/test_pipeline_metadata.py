import time

from edqp.ingestion.ingestion_engine import IngestionEngine

from edqp.validation.validation_engine import ValidationEngine
from edqp.validation.rules.null_rule import NullRule
from edqp.validation.rules.duplicate_rule import DuplicateRule
from edqp.validation.rules.email_rule import EmailRule
from edqp.validation.rules.range_rule import RangeRule

from edqp.reporting.validation_report import ValidationReport

from edqp.metadata.pipeline_metadata import PipelineMetadata
from edqp.metadata.metadata_writer import MetadataWriter


def main():

    start = time.perf_counter()

    ingestion = IngestionEngine()

    df = ingestion.read("datasets/raw/customers.csv")

    engine = ValidationEngine()

    engine.add_rule(
        "Null Email",
        NullRule(),
        column="email",
    )

    engine.add_rule(
        "Duplicate Customer",
        DuplicateRule(),
        columns=["name", "email"],
    )

    engine.add_rule(
        "Invalid Email",
        EmailRule(),
        column="email",
    )

    engine.add_rule(
        "Invalid Age",
        RangeRule(),
        column="age",
        minimum=0,
    )

    validation_results = engine.run(df)

    report = ValidationReport().generate(
        dataset_name="customers.csv",
        df=df,
        validation_results=validation_results,
    )

    execution_time = time.perf_counter() - start

    metadata = PipelineMetadata().create(
        report=report,
        execution_time=execution_time,
    )

    writer = MetadataWriter()

    writer.save(
        metadata,
        "metadata/pipeline_runs.parquet",
    )


if __name__ == "__main__":
    main()