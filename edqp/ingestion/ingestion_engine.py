from pathlib import Path

import polars as pl


class IngestionEngine:
    """
    Reads datasets into a Polars DataFrame.
    Currently supports CSV files.
    """

    def read(self, file_path: str) -> pl.DataFrame:
        path = Path(file_path)

        if not path.exists():
            raise FileNotFoundError(f"File not found: {file_path}")

        if path.suffix.lower() == ".csv":
            return pl.read_csv(path)

        raise ValueError(f"Unsupported file type: {path.suffix}")