from edqp.tracking.pipeline_tracker import PipelineTracker


def main():

    tracker = PipelineTracker()

    filename = "customers.csv"

    print("Already processed:",
          tracker.is_processed(filename))

    tracker.mark_processed(filename)

    print("Already processed:",
          tracker.is_processed(filename))


if __name__ == "__main__":
    main()