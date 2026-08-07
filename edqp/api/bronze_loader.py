import polars as pl


class BronzeLoader:

    def save(
        self,
        data,
        output_path: str,
    ):

        df = pl.DataFrame(data)

        df.write_parquet(output_path)

        print(f"Saved: {output_path}")