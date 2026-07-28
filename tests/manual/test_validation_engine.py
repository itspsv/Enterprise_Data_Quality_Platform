from edqp.ingestion.ingestion_engine import IngestionEngine

from edqp.validation.validation_engine import ValidationEngine

from edqp.validation.rules.null_rule import NullRule
from edqp.validation.rules.duplicate_rule import DuplicateRule
from edqp.validation.rules.email_rule import EmailRule
from edqp.validation.rules.range_rule import RangeRule


def main():
    ingestion = IngestionEngine()
    df = ingestion.read("datasets/raw/customers.csv")

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

    results = engine.run(df)

    print("=" * 60)

    for rule_name, invalid_rows in results.items():
        print(f"\n{rule_name}")
        print("-" * 60)
        print(invalid_rows)


if __name__ == "__main__":
    main()