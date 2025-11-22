from set_ips import addresses
from ssh_helpers import hosts

"""
adds a new vlan aware bridge on the host
by default, vlan_filtering is active
for the internal interfaces, all vlans will be allowed
all other interfaces on the host will not be usable until configured with set_vlan(...)
"""


def setup_bridge(host, internal_interfaces, bridge_name="br0"):
    host.run(
        f"ip link add name {bridge_name} type bridge vlan_filtering 1 vlan_default_pvid 0"
    )
    host.set_interface_up(bridge_name)
    for interface in [f"eth{n}" for n in [1, 2, 3, 4]]:
        host.run(f"ip addr flush dev {interface}")
        host.run(f"ip link set {interface} master {bridge_name}")
    for interface in internal_interfaces:
        host.run(f"bridge vlan add vid 1-4094 dev {interface}")


"""
external_interfaces: List of Tuple(host, interface_name)

Setup a vlan path between the external interfaces.
The external_interfaces will afterwards be able to communicate.
The traffic will be sent vlan tagged via the bridges.
On the external interfaces, the ingress and egress frames will be untagged.
"""


def set_vlan(vlanid, external_interfaces):
    for host, interface in external_interfaces:
        host.run(f"bridge vlan add vid {vlanid} dev {interface} pvid untagged")


setup_bridge(
    host=hosts["router1"],
    internal_interfaces=["eth3"],  # connection to router3
)

setup_bridge(
    host=hosts["router2"],
    internal_interfaces=["eth3"],  # connection to router3
)

setup_bridge(
    host=hosts["router3"],
    internal_interfaces=["eth2", "eth3"],  # connection to router1 and 2
)

set_vlan(
    vlanid=12,
    external_interfaces=[
        (hosts["router1"], "eth1"),  # port connecting to pc1
        (hosts["router2"], "eth1"),  # port connecting to pc2
    ],
)

set_vlan(
    vlanid=34,
    external_interfaces=[
        (hosts["router3"], "eth1"),  # port connecting to pc3
        (hosts["router1"], "eth4"),  # port connecting to router4
    ],
)
