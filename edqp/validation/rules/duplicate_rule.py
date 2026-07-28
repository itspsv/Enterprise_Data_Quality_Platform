import polars as pl


class DuplicateRule:
    """
    Checks for duplicate records based on specified columns.
    """

    def validate(self, df: pl.DataFrame, columns: list[str]) -> pl.DataFrame:
        """
        Returns all duplicate rows based on the given columns.
        """
        return df.filter(pl.struct(columns).is_duplicated())