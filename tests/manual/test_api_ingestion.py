from edqp.api.api_client import APIClient
from edqp.api.bronze_loader import BronzeLoader


def main():

    client = APIClient()

    products = client.fetch(
        "https://fakestoreapi.com/products"
    )

    users = client.fetch(
        "https://fakestoreapi.com/users"
    )

    BronzeLoader().save(
        products,
        "datasets/bronze/products.parquet",
    )

    BronzeLoader().save(
        users,
        "datasets/bronze/users.parquet",
    )


if __name__ == "__main__":
    main()