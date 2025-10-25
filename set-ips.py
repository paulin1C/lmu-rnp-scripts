from ssh_helpers import hosts

prefix = "10.153.211"

addresses = {
    "router1": {
        "eth1": f"{prefix}.011",
        "eth2": f"{prefix}.012",
        "eth3": f"{prefix}.013",
        "eth4": f"{prefix}.014",
    },
    "router2": {
        "eth1": f"{prefix}.021",
        "eth2": f"{prefix}.022",
        "eth3": f"{prefix}.023",
        "eth4": f"{prefix}.024",
    },
    "router3": {
        "eth1": f"{prefix}.031",
        "eth2": f"{prefix}.032",
        "eth3": f"{prefix}.033",
        "eth4": f"{prefix}.034",
    },
    "router4": {
        "eth1": f"{prefix}.041",
        "eth2": f"{prefix}.042",
        "eth3": f"{prefix}.043",
        "eth4": f"{prefix}.044",
    },
    "pc1": {
        "eth1": f"{prefix}.111",
    },
    "pc2": {
        "eth1": f"{prefix}.121",
    },
    "pc3": {
        "eth1": f"{prefix}.131",
    },
}

for host in hosts.values():
    for interface, address in addresses[host.name].items():
        host.set_interface_address(interface, address)
        host.set_interface_up(interface)
