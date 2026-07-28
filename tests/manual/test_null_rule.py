from edqp.ingestion.ingestion_engine import IngestionEngine
from edqp.validation.rules.null_rule import NullRule


def main():
    ingestion = IngestionEngine()
    df = ingestion.read("datasets/raw/customers.csv")

    null_rule = NullRule()

    null_rows = null_rule.validate(df, "email")

    print("=" * 50)
    print("Rows with Missing Email")
    print("=" * 50)
    print(null_rows)


if __name__ == "__main__":
    main()