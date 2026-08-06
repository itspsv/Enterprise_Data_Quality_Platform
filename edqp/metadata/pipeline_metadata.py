from datetime import datetime


class PipelineMetadata:
    """
    Generates metadata for each pipeline execution.
    """

    def create(
        self,
        report,
        execution_time,
    ):

        metadata = {
            "timestamp": datetime.now().strftime("%Y-%m-%d %H:%M:%S"),
            "dataset": report["dataset"],
            "total_rows": report["total_rows"],
            "valid_rows": report["valid_rows"],
            "invalid_rows": report["invalid_rows"],
            "quality_score": report["quality_score"],
            "execution_time_seconds": round(execution_time, 2),
            "rule_failures": report["rules"],
        }

        return metadata