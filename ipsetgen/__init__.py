from . import config
import subprocess


class IPSet(object):
    def __init__(self, ipsets, ipset_cmd=None):
        if ipset_cmd is None:
            self.ipset_cmd = 'ipset'
        else:
            self.ipset_cmd = ipset_cmd
        _ = subprocess.check_output((ipset_cmd, '-v'))

    def generate_set(self, set_name):
        _destroy = (self.ipset_cmd, 'destroy', set_name)

        _ = subprocess.check_output(_destroy)
