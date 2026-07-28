from edqp.ingestion.ingestion_engine import IngestionEngine
from edqp.validation.rules.null_rule import NullRule


def main():
    # Read dataset
    ingestion = IngestionEngine()
    df = ingestion.read("datasets/raw/customers.csv")

    # Run Null Rule on the email column
    null_rule = NullRule()
    invalid_rows = null_rule.validate(df, "email")

    print("=" * 50)
    print("Rows with Missing Email")
    print("=" * 50)
    print(invalid_rows)


if __name__ == "__main__":
    main()