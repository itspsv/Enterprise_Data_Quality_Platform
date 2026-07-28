from edqp.ingestion.ingestion_engine import IngestionEngine
from edqp.validation.rules.duplicate_rule import DuplicateRule


def main():
    ingestion = IngestionEngine()
    df = ingestion.read("datasets/raw/customers.csv")

    duplicate_rule = DuplicateRule()

    duplicates = duplicate_rule.validate(
        df,
        ["name", "email"]
    )

    print("=" * 50)
    print("Duplicate Records")
    print("=" * 50)
    print(duplicates)


if __name__ == "__main__":
    main()