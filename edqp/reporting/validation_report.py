import polars as pl
from datetime import datetime


class ValidationReport:
    """
    Generates a summary report from validation results.
    """

    def generate(
        self,
        dataset_name: str,
        df: pl.DataFrame,
        validation_results: dict,
    ) -> dict:

        total_rows = df.height

        total_invalid = 0

        report = {
            "dataset": dataset_name,
            "generated_at": datetime.now().strftime("%Y-%m-%d %H:%M:%S"),
            "total_rows": total_rows,
            "rules": {}
        }

        for rule_name, invalid_rows in validation_results.items():

            count = invalid_rows.height

            report["rules"][rule_name] = count

            total_invalid += count

        valid_rows = max(total_rows - total_invalid, 0)

        quality_score = round(
            (valid_rows / total_rows) * 100,
            2
        ) if total_rows > 0 else 0

        report["valid_rows"] = valid_rows
        report["invalid_rows"] = total_invalid
        report["quality_score"] = quality_score

        return report