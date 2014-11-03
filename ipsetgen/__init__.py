from warnings import warn
import ipaddress
import subprocess


class IPSet(object):
    def __init__(self, role, ipset_cmd=None):
        if ipset_cmd is None:
            self.ipset_cmd = 'ipset'
        else:
            self.ipset_cmd = ipset_cmd
        subprocess.check_output((ipset_cmd, '-v'),
                                universal_newlines=True,
                                stdout=subprocess.DEVNULL)

        self.role = role
        self.services = role.services

    def _enumerate_role_addresses(self, role=None):
        if role is None:
            _role = self.role
        else:
            _role = role

        for service in _role.services:
            for address in service.addresses:
                yield address

    def generate_set(self, set_name):
        _create = (self.ipset_cmd, 'create', set_name, 'hash:ip')

    def destroy_set(self, set_name):
        _destroy = (self.ipset_cmd, 'destroy', set_name)
        p = subprocess.Popen(_destroy,
                             universal_newlines=True,
                             stderr=subprocess.PIPE)
        _, err = p.communicate()
        if 'The set with the given name does not exist' in err:
            pass
        else:
            raise FileNotFoundError(
                'Error running {}. Is ipset installed?'.format(
                    ' '.join(_destroy)))
        return True


class Role(object):
    def __init__(self, name, services):
        self.name = name
        self.services = services


class Service(object):
    def __init__(self, name, addrs=[]):
        self.name = name
        self.addresses = map(self._validate_address, addrs)

    def __str__(self):
        return self.name

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
