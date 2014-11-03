import os
import yaml


_DEFAULT_CONFIG_PATH = '/etc/ipsetgen/'


class Config(object):
    def __init__(self, config_path=_DEFAULT_CONFIG_PATH):
        self.config_path = config_path
        self.configs = self._load_all_files()

    def _load_all_files(self):
        for config_file in os.listdir(self.config_path):
            if os.path.isfile(self.config_path + config_file)
            with open(self.config_path + config_file, 'r') as fh:
                yield yaml.load(fh)
