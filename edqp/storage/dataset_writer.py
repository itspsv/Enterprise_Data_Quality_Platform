from pathlib import Path

import polars as pl


class DatasetWriter:
    """
    Saves datasets to disk.
    """

    def save_parquet(
        self,
        df: pl.DataFrame,
        output_path: str,
    ) -> None:

        path = Path(output_path)

        # Create parent folders if they don't exist
        path.parent.mkdir(parents=True, exist_ok=True)

        df.write_parquet(path)

        print(f"Dataset saved to: {path}")