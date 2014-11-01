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


class Service(object):
    def __init__(self, service, ports=None):
        self.service = service
        self.ports = ports

class Port(object):
    def __init__(self, port, rules):
        self.port = port
        self.rules = rules

class Rule(object):
    def __init__(self, rule, roles):
        self.rule = rule
        self.roles = roles

class Role(object):
    def __init__(self, name, ipv4_addrs=[], ipv6_addrs=[]):
        self.name = name
        self.ipv4_addrs = ipv4_addrs
        self.ipv6_addrs = ipv6_addrs
