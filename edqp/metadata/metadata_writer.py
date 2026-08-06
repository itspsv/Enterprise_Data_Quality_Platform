import os

import polars as pl


class MetadataWriter:
    """
    Saves pipeline execution metadata.
    """

    def save(
        self,
        metadata: dict,
        output_path: str,
    ):

        os.makedirs(os.path.dirname(output_path), exist_ok=True)

        new_metadata = pl.DataFrame([metadata])

        if os.path.exists(output_path):

            existing = pl.read_parquet(output_path)

            metadata_df = pl.concat(
                [existing, new_metadata],
                how="diagonal",
            )

        else:

            metadata_df = new_metadata

        metadata_df.write_parquet(output_path)

        print(f"Metadata saved to: {output_path}")