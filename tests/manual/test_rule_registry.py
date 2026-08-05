from edqp.config.config_loader import ConfigLoader

from edqp.ingestion.ingestion_engine import IngestionEngine

from edqp.registry.rule_registry import RuleRegistry

from edqp.validation.validation_engine import ValidationEngine


def main():

    config = ConfigLoader().get()

    ingestion = IngestionEngine()

    df = ingestion.read("datasets/raw/customers.csv")

    engine = ValidationEngine()

    RuleRegistry().register(
        engine,
        config["validation"],
    )

    results = engine.run(df)

    print("=" * 60)

    for rule_name, result in results.items():

        print(rule_name)
        print(result["rows"])
        print()


if __name__ == "__main__":
    main()