from pathlib import Path
import yaml


class ConfigLoader:
    """
    Loads the project configuration from settings.yaml
    """

    def __init__(self):
        project_root = Path(__file__).resolve().parents[2]
        config_path = project_root / "edqp" / "config" / "settings.yaml"

        with open(config_path, "r") as file:
            self.config = yaml.safe_load(file)

    def get(self):
        return self.config