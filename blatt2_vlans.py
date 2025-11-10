from set_ips import addresses
from ssh_helpers import hosts


def set_vlan(host, interface, vlanid):
    dev_name = f"{interface}.{vlanid}"
    host.run(f"ip addr flush dev {interface}")
    host.run(f"ip link add link {interface} name {dev_name} type vlan id {vlanid}")
    host.add_interface_address(dev_name, addresses[host.name][interface])
    host.set_interface_up(dev_name)


set_vlan(hosts["pc1"], "eth1", 100)
set_vlan(hosts["pc2"], "eth1", 100)

set_vlan(hosts["router4"], "eth1", 20)
set_vlan(hosts["pc3"], "eth1", 20)
