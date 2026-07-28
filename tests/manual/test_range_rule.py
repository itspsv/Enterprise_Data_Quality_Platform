from edqp.ingestion.ingestion_engine import IngestionEngine
from edqp.validation.rules.range_rule import RangeRule


def main():
    ingestion = IngestionEngine()
    df = ingestion.read("datasets/raw/customers.csv")

    range_rule = RangeRule()

    invalid_age = range_rule.validate(
        df,
        column="age",
        minimum=0
    )

    print("=" * 50)
    print("Invalid Age Records")
    print("=" * 50)
    print(invalid_age)


if __name__ == "__main__":
    main()