from ssh_helpers import hosts

prefix = "10.153.211"

addresses = {
    "router1": {
        "eth1": f"{prefix}.211",
        "eth2": f"{prefix}.212",
        "eth3": f"{prefix}.213",
        "eth4": f"{prefix}.214",
    },
    "router2": {
        "eth1": f"{prefix}.221",
        "eth2": f"{prefix}.222",
        "eth3": f"{prefix}.223",
        "eth4": f"{prefix}.224",
    },
    "router3": {
        "eth1": f"{prefix}.231",
        "eth2": f"{prefix}.232",
        "eth3": f"{prefix}.233",
        "eth4": f"{prefix}.234",
    },
    "router4": {
        "eth1": f"{prefix}.241",
        "eth2": f"{prefix}.242",
        "eth3": f"{prefix}.243",
        "eth4": f"{prefix}.244",
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


if __name__ == "__main__":
    for host in hosts.values():
        for interface, address in addresses[host.name].items():
            host.add_interface_address(interface, address)
            host.set_interface_up(interface)
