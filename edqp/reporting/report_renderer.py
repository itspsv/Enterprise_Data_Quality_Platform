from edqp.logging.logger import PipelineLogger


class ReportRenderer:

    def __init__(self):

        self.logger = PipelineLogger().get_logger()

    def display(self, report):

        self.logger.info("=" * 60)
        self.logger.info("Validation Report")
        self.logger.info("=" * 60)

        self.logger.info(f"Dataset         : {report['dataset']}")
        self.logger.info(f"Generated At    : {report['generated_at']}")
        self.logger.info("")

        self.logger.info(f"Total Rows      : {report['total_rows']}")
        self.logger.info(f"Valid Rows      : {report['valid_rows']}")
        self.logger.info(f"Invalid Rows    : {report['invalid_rows']}")
        self.logger.info("")

        self.logger.info(
            f"Quality Score   : {report['quality_score']:.2f}%"
        )

        self.logger.info("")
        self.logger.info("Validation Rules")
        self.logger.info("-" * 60)

        for rule_name, failed_rows in report["rules"].items():
            self.logger.info(f"{rule_name:<25}: {failed_rows}")