from edqp.logging.logger import PipelineLogger


def main():

    logger = PipelineLogger().get_logger()

    logger.info("Pipeline started")

    logger.warning("This is a warning")

    logger.error("This is an error")

    logger.success("Pipeline completed")


if __name__ == "__main__":
    main()