import polars as pl

from edqp.validation.rules.null_rule import NullRule


def test_null_rule():

    df = pl.DataFrame(
        {
            "id": [1, 2, 3],
            "email": [
                "a@gmail.com",
                None,
                "c@gmail.com",
            ],
        }
    )

    rule = NullRule()

    result = rule.validate(
        df,
        "email",
    )

    assert result.height == 1