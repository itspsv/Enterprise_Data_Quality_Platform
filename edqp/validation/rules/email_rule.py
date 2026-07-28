import re
import polars as pl


class EmailRule:
    """
    Checks for invalid email addresses in a specified column.
    """

    EMAIL_PATTERN = r"^[A-Za-z0-9._%+-]+@[A-Za-z0-9.-]+\.[A-Za-z]{2,}$"

    def validate(self, df: pl.DataFrame, column: str) -> pl.DataFrame:
        """
        Returns rows containing invalid email addresses.
        Null values are ignored because NullRule handles them.
        """
        return df.filter(
            pl.col(column).is_not_null()
            & (~pl.col(column).str.contains(self.EMAIL_PATTERN))
        )