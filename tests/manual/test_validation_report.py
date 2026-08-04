from edqp.ingestion.ingestion_engine import IngestionEngine

from edqp.validation.validation_engine import ValidationEngine
from edqp.validation.rules.null_rule import NullRule
from edqp.validation.rules.duplicate_rule import DuplicateRule
from edqp.validation.rules.email_rule import EmailRule
from edqp.validation.rules.range_rule import RangeRule

from edqp.reporting.validation_report import ValidationReport
from edqp.reporting.report_renderer import ReportRenderer


def main():

    # Read dataset
    ingestion = IngestionEngine()
    df = ingestion.read("datasets/raw/customers.csv")

    # Run validations
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

    # Generate report
    report = ValidationReport().generate(
        dataset_name="customers.csv",
        df=df,
        validation_results=validation_results
    )

    # Display report
    renderer = ReportRenderer()
    renderer.display(report)


if __name__ == "__main__":
    main()