'''
Design a Python class called 'Router' that models a network router
with properties like 'model', 'manufacturer', and 'IP_address'.
Include methods to configure the router and display its configuration.

The Router should have the ability to add and remove interfaces.
Implement exception handling for invalid IP addresses.
'''
import re


class InvalidIPAddressError(Exception):
    pass


class Router:
    model = 'dlink'

    def __new__(cls, model, manufacturer=None, IP_address=None):
        if IP_address == "255.0.0.0":
            raise Exception("IP address can't be, {}".format(IP_address))
        # you need to ensure that __new__ returns an instance of the class
        return super(Router, cls).__new__(cls)

    def __init__(self, model, manufacturer=None, IP_address=None):
        self.interfaces = []
        self.model = model
        if manufacturer:
            self.manufacturer = manufacturer
        if IP_address:
            self.ip_address = IP_address
            self.validate_ip_address(self.ip_address)

    @staticmethod
    def validate_ip_address(ip_address):
        pattern = re.compile(r"^(?:[0-9]{1,3}\.){3}[0-9]{1,3}$")
        if not pattern.match(ip_address):
            raise InvalidIPAddressError(f"Invalid IP address: {ip_address}")

    def add_interface(self, interface):
        if interface not in self.interfaces:
            self.interfaces.append(interface)

    def remove_interface(self, interface):
        if interface in self.interfaces:
            self.interfaces.remove(interface)


# Because __new__ returns class instance,
# the 'router' variable (below) is assigned to the class instance or class object
ipaddress = "255.000.000.000"
router = Router(model="tplink6e10", manufacturer="Tplink", IP_address=ipaddress)

print(router.model)
