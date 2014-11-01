import os
import yaml


def _load_all_files(self):
    for config_file in os.listdir(self.config_path):
        with open(config_file, 'r') as fh:
            yield yaml.load(fh)
