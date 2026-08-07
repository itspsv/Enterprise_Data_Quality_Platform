import random
from datetime import datetime

import polars as pl


class OrderGenerator:

    def generate(
        self,
        users_df: pl.DataFrame,
        products_df: pl.DataFrame,
        n_orders: int = 100,
    ) -> pl.DataFrame:

        users = users_df["id"].to_list()
        products = products_df.select(
            ["id", "price"]
        ).to_dicts()

        orders = []

        for order_id in range(1, n_orders + 1):

            product = random.choice(products)

            orders.append(
                {
                    "order_id": order_id,
                    "user_id": random.choice(users),
                    "product_id": product["id"],
                    "quantity": random.randint(1, 5),
                    "unit_price": product["price"],
                    "order_timestamp": datetime.now().isoformat(),
                }
            )

        return pl.DataFrame(orders)