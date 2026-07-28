import polars as pl


class NullRule:
    """
    Checks for null values in a specified column.
    """

    def validate(self, df: pl.DataFrame, column: str) -> pl.DataFrame:
        """
        Returns all rows where the specified column contains null values.
        """
        return df.filter(pl.col(column).is_null())