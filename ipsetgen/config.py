import os
import yaml


_DEFAULT_CONFIG_PATH = '/etc/ipsetgen/'


def _load_all_files(path):
    for config_file in os.listdir(path):
        with open(config_file, 'r') as fh:
            yield yaml.load(fh)


class Config(object):
    def __init__(self, config_path=_DEFAULT_CONFIG_PATH):
        self.config_path = config_path
        self.configs = _load_all_files(self.config_path)


class Port(object):
    def __init__(self, port, rules):
        self.port = port
        self.rules = rules


class Rule(object):
    def __init__(self, rule, roles):
        self.rule = rule
        self.roles = roles
