import os


class Host:
    def __init__(self, name):
        self.name = name

    def run(self, cmd):
        print(f"Host {self.name}: running '{cmd}'")
        run_cmd_on_vm_host(f"ssh -t {self.name} '{cmd}'")

    def add_interface_address(self, interace, address, cdir="/24"):
        self.run(f"ip addr add {address}{cdir} dev {interace}")

    def set_interface_up(self, interface):
        self.set_interface(interface, "up")

    def set_interface(self, interface, state="up"):
        self.run(f"ip link set dev {interface} {state}")


def run_cmd_on_vm_host(cmd):
    os.system(f"ssh -t rnp-cip '{cmd}'")


routers = {
    "router1": Host("router1"),
    "router2": Host("router2"),
    "router3": Host("router3"),
    "router4": Host("router4"),
}

pcs = {
    "pc1": Host("pc1"),
    "pc2": Host("pc2"),
    "pc3": Host("pc3"),
}

hosts = dict(routers, **pcs)
