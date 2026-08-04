from edqp.ingestion.ingestion_engine import IngestionEngine

from edqp.validation.validation_engine import ValidationEngine
from edqp.validation.rules.null_rule import NullRule
from edqp.validation.rules.duplicate_rule import DuplicateRule
from edqp.validation.rules.email_rule import EmailRule
from edqp.validation.rules.range_rule import RangeRule

from edqp.reporting.validation_report import ValidationReport
from edqp.reporting.report_renderer import ReportRenderer

from edqp.processing.data_separator import DataSeparator

from edqp.storage.dataset_writer import DatasetWriter


def main():

    # -----------------------------
    # Read Dataset
    # -----------------------------
    ingestion = IngestionEngine()

    df = ingestion.read("datasets/raw/customers.csv")

    # -----------------------------
    # Validation
    # -----------------------------
    engine = ValidationEngine()

    engine.add_rule(
        "Null Email",
        NullRule(),
        column="email"
    )

    engine.add_rule(
        "Duplicate Customer",
        DuplicateRule(),
        columns=["name", "email"]
    )

    engine.add_rule(
        "Invalid Email",
        EmailRule(),
        column="email"
    )

    engine.add_rule(
        "Invalid Age",
        RangeRule(),
        column="age",
        minimum=0
    )

    validation_results = engine.run(df)

    # -----------------------------
    # Validation Report
    # -----------------------------
    report = ValidationReport().generate(
        dataset_name="customers.csv",
        df=df,
        validation_results=validation_results,
    )

    renderer = ReportRenderer()

    renderer.display(report)

    # -----------------------------
    # Split Data
    # -----------------------------
    separator = DataSeparator()

    valid_df, invalid_df = separator.split(
        df=df,
        failed_ids=report["failed_ids"],
        primary_key="customer_id",
    )

    # -----------------------------
    # Save Data
    # -----------------------------
    writer = DatasetWriter()

    writer.save_parquet(
        valid_df,
        "datasets/silver/customers.parquet",
    )

    writer.save_parquet(
        invalid_df,
        "datasets/quarantine/customers.parquet",
    )


if __name__ == "__main__":
    main()