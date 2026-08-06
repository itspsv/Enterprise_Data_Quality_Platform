class QualitySummary:
    """
    Generates an AI-style summary from the validation report.
    """

    def generate(self, report: dict) -> str:

        quality = report["quality_score"]

        if quality >= 95:
            health = "Excellent"

        elif quality >= 80:
            health = "Good"

        elif quality >= 60:
            health = "Fair"

        else:
            health = "Poor"

        rule_lines = []

        for rule, count in report["rules"].items():
            if count > 0:
                rule_lines.append(
                    f"- {rule}: {count} failed records"
                )

        summary = f"""
Pipeline Health: {health}

Dataset: {report['dataset']}

Quality Score: {quality:.2f}%

Valid Rows: {report['valid_rows']}

Invalid Rows: {report['invalid_rows']}

Validation Issues:

{chr(10).join(rule_lines)}

Recommendation:

Review the failed records before promoting the dataset to production.
"""

        return summary.strip()