from pathlib import Path

import polars as pl


class MetadataWriter:
    """
    Saves pipeline metadata and appends new runs.
    """

    def save(
        self,
        metadata: pl.DataFrame,
        output_path: str,
    ) -> None:

        path = Path(output_path)

        path.parent.mkdir(parents=True, exist_ok=True)

        if path.exists():

            existing = pl.read_parquet(path)

            metadata = pl.concat([existing, metadata])

        metadata.write_parquet(path)

        print(f"Metadata saved to: {path}")