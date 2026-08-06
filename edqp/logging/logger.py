import os
import sys

from loguru import logger


class PipelineLogger:

    def __init__(self):

        logger.remove()

        os.makedirs("logs", exist_ok=True)

        logger.add(
            sys.stdout,
            level="INFO",
            format="{time:YYYY-MM-DD HH:mm:ss} | {level:<8} | {message}",
        )

        logger.add(
            "logs/pipeline.log",
            rotation="10 MB",
            retention=10,
            level="INFO",
            format="{time:YYYY-MM-DD HH:mm:ss} | {level:<8} | {message}",
        )

        self.logger = logger

    def get_logger(self):
        return self.logger