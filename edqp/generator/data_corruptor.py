import polars as pl


class DataCorruptor:

    def corrupt(
        self,
        df: pl.DataFrame,
    ) -> pl.DataFrame:

        rows = df.to_dicts()

        if len(rows) < 10:
            return df

        # Null user_id
        rows[5]["user_id"] = None

        # Negative price
        rows[10]["unit_price"] = -50

        # Invalid quantity
        rows[15]["quantity"] = 0

        # Missing timestamp
        rows[20]["order_timestamp"] = None

        # Duplicate order
        rows.append(rows[25].copy())

        return pl.DataFrame(rows)