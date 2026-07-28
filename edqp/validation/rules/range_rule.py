import polars as pl


class RangeRule:
    """
    Checks whether numeric values fall within a specified range.
    """

    def validate(
        self,
        df: pl.DataFrame,
        column: str,
        minimum=None,
        maximum=None,
    ) -> pl.DataFrame:
        """
        Returns rows that violate the specified range.
        """
        condition = pl.lit(False)

        if minimum is not None:
            condition = condition | (pl.col(column) < minimum)

        if maximum is not None:
            condition = condition | (pl.col(column) > maximum)

        return df.filter(condition)