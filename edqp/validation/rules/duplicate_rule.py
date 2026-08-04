import polars as pl


class DuplicateRule:
    """
    Detect duplicate records while keeping the first occurrence.
    Only subsequent duplicates are returned.
    """

    def validate(self, df: pl.DataFrame, columns: list[str]) -> pl.DataFrame:
        """
        Returns duplicate rows excluding the first occurrence.
        """

        # Mark duplicate occurrences while keeping the first record
        duplicate_mask = (
            df.with_columns(
                pl.struct(columns)
                .is_duplicated()
                .alias("is_duplicate")
            )
            .with_columns(
                pl.struct(columns)
                .cum_count()
                .over(columns)
                .alias("occurrence")
            )
            .filter(
                (pl.col("is_duplicate")) &
                (pl.col("occurrence") > 1)
            )
            .drop(["is_duplicate", "occurrence"])
        )

        return duplicate_mask