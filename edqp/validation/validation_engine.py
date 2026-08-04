import polars as pl


class ValidationEngine:
    """
    Executes multiple validation rules and collects the results.
    """

    def __init__(self):
        self.rules = []

    def add_rule(self, name: str, rule, **kwargs):
        """
        Register a validation rule.
        """
        self.rules.append(
            {
                "name": name,
                "rule": rule,
                "kwargs": kwargs,
            }
        )

    def run(self, df: pl.DataFrame):
        """
        Execute all registered rules.
        """
        results = {}

        for item in self.rules:

            invalid_rows = item["rule"].validate(
                df,
                **item["kwargs"]
            )

            results[item["name"]] = {
                "rows": invalid_rows,
                "count": invalid_rows.height,
                "indices": set(invalid_rows.get_column("customer_id").to_list())
            }

        return results