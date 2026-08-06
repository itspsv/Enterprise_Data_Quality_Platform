import json
import os


class PipelineTracker:
    """
    Tracks which datasets have already been processed.
    """

    def __init__(self):

        self.file = "metadata/processed_files.json"

        if not os.path.exists(self.file):

            os.makedirs("metadata", exist_ok=True)

            with open(self.file, "w") as f:
                json.dump([], f)

    def is_processed(self, filename):

        with open(self.file, "r") as f:
            processed = json.load(f)

        return filename in processed

    def mark_processed(self, filename):

        with open(self.file, "r") as f:
            processed = json.load(f)

        if filename not in processed:

            processed.append(filename)

            with open(self.file, "w") as f:
                json.dump(processed, f, indent=4)