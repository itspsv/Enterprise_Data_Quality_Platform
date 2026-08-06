from edqp.ai.quality_summary import QualitySummary
from edqp.reporting.validation_report import ValidationReport
from edqp.ingestion.ingestion_engine import IngestionEngine
from edqp.registry.rule_registry import RuleRegistry
from edqp.validation.validation_engine import ValidationEngine
from edqp.config.config_loader import ConfigLoader


def main():

    config = ConfigLoader().get()

    df = IngestionEngine().read("datasets/raw/customers.csv")

    engine = ValidationEngine()

    RuleRegistry().register(
        engine,
        config["validation"],
    )

    results = engine.run(df)

    report = ValidationReport().generate(
        dataset_name="customers.csv",
        df=df,
        validation_results=results,
    )

    summary = QualitySummary().generate(report)

    print(summary)


if __name__ == "__main__":
    main()