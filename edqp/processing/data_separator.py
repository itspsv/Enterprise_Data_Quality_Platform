import polars as pl


class DataSeparator:
    """
    Splits a dataset into valid and invalid records.
    """

    def split(
        self,
        df: pl.DataFrame,
        failed_ids: set,
        primary_key: str,
    ):

        invalid_df = df.filter(
            pl.col(primary_key).is_in(failed_ids)
        )

        valid_df = df.filter(
            ~pl.col(primary_key).is_in(failed_ids)
        )

        return valid_df, invalid_df