from edqp.ingestion.ingestion_engine import IngestionEngine
from edqp.validation.rules.email_rule import EmailRule


def main():
    ingestion = IngestionEngine()
    df = ingestion.read("datasets/raw/customers.csv")

    email_rule = EmailRule()

    invalid_emails = email_rule.validate(df, "email")

    print("=" * 50)
    print("Invalid Email Addresses")
    print("=" * 50)
    print(invalid_emails)


if __name__ == "__main__":
    main()