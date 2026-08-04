from datetime import datetime
import uuid

import polars as pl


class PipelineMetadata:
    """
    Creates metadata for each pipeline execution.
    """

    def create(
        self,
        report: dict,
        execution_time: float,
    ) -> pl.DataFrame:

        metadata = pl.DataFrame(
            {
                "run_id": [str(uuid.uuid4())],
                "timestamp": [datetime.now().strftime("%Y-%m-%d %H:%M:%S")],
                "dataset": [report["dataset"]],
                "total_rows": [report["total_rows"]],
                "valid_rows": [report["valid_rows"]],
                "invalid_rows": [report["invalid_rows"]],
                "quality_score": [report["quality_score"]],
                "execution_time_seconds": [round(execution_time, 3)],
                "status": ["SUCCESS"],
            }
        )

        return metadata