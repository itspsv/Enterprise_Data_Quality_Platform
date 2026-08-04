from datetime import datetime

import polars as pl


class ValidationReport:
    """
    Generates a validation summary report.
    """

    def generate(
        self,
        dataset_name: str,
        df: pl.DataFrame,
        validation_results: dict,
    ) -> dict:

        total_rows = df.height

        failed_ids = set()

        rule_summary = {}

        for rule_name, result in validation_results.items():

            rule_summary[rule_name] = result["count"]

            failed_ids.update(result["indices"])

        invalid_rows = len(failed_ids)

        valid_rows = total_rows - invalid_rows

        quality_score = (
            round((valid_rows / total_rows) * 100, 2)
            if total_rows > 0
            else 0
        )

        report = {
            "dataset": dataset_name,
            "generated_at": datetime.now().strftime("%Y-%m-%d %H:%M:%S"),
            "total_rows": total_rows,
            "valid_rows": valid_rows,
            "invalid_rows": invalid_rows,
            "quality_score": quality_score,
            "failed_ids": failed_ids,
            "rules": rule_summary,
        }

        return report