import polars as pl

from edqp.generator.order_generator import OrderGenerator


def main():

    users = pl.read_parquet(
        "datasets/bronze/users.parquet"
    )

    products = pl.read_parquet(
        "datasets/bronze/products.parquet"
    )

    orders = OrderGenerator().generate(
        users,
        products,
        n_orders=100,
    )

    print(orders.head())

    orders.write_parquet(
        "datasets/bronze/orders.parquet"
    )

    print(
        "\nSaved: datasets/bronze/orders.parquet"
    )


if __name__ == "__main__":
    main()