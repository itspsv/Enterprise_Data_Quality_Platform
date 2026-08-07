import polars as pl

from edqp.validation.validation_engine import ValidationEngine
from edqp.validation.rules.null_rule import NullRule
from edqp.validation.rules.duplicate_rule import DuplicateRule
from edqp.validation.rules.range_rule import RangeRule


def main():

    df = pl.read_parquet(
        "datasets/bronze/orders_dirty.parquet"
    )

    engine = ValidationEngine(
        primary_key="order_id"
    )

    engine.add_rule(
        name="Null User",
        rule=NullRule(),
        column="user_id",
    )

    engine.add_rule(
        name="Duplicate Order",
        rule=DuplicateRule(),
        columns=["order_id"],
    )

    engine.add_rule(
        name="Invalid Quantity",
        rule=RangeRule(),
        column="quantity",
        minimum=1,
    )

    engine.add_rule(
        name="Negative Price",
        rule=RangeRule(),
        column="unit_price",
        minimum=0,
    )

    engine.add_rule(
        name="Missing Timestamp",
        rule=NullRule(),
        column="order_timestamp",
    )

    results = engine.run(df)

    for rule, result in results.items():

        print(
            f"{rule}: {result['count']}"
        )


if __name__ == "__main__":
    main()