import polars as pl

from edqp.generator.data_corruptor import DataCorruptor


def main():

    orders = pl.read_parquet(
        "datasets/bronze/orders.parquet"
    )

    dirty_orders = DataCorruptor().corrupt(
        orders
    )

    dirty_orders.write_parquet(
        "datasets/bronze/orders_dirty.parquet"
    )

    print(dirty_orders.shape)

    print(
        "\nSaved: datasets/bronze/orders_dirty.parquet"
    )


if __name__ == "__main__":
    main()