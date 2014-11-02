from warnings import warn
import ipaddress
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
    def __init__(self, name, addrs=[]):
        self.name = name
        self.addresses = map(self._validate_address, addrs)

    def _validate_address(self, address):
        try:
            if '/' in address:
                addr = ipaddress.ip_network(address)
            else:
                addr = ipaddress.ip_address(address)
        except ValueError:
            warn('{} is not a valid address or network, ignoring.'.format(
                address))
        return addr
