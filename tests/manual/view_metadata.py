import polars as pl

df = pl.read_parquet("metadata/pipeline_runs.parquet")

print(df)