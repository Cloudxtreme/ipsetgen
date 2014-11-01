import os
import yaml


def _load_all_files(self):
    for config_file in os.listdir(self.config_path):
        with open(config_file, 'r') as fh:
            yield yaml.load(fh)


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
