from ssh_helpers import hosts

ifstates = {
    "router1": {
        "eth1": "up",
        "eth2": "down",
        "eth3": "up",
        "eth4": "up",
    },
    "router2": {
        "eth1": "up",
        "eth2": "down",
        "eth3": "up",
        "eth4": "down",
    },
    "router3": {
        "eth1": "up",
        "eth2": "up",
        "eth3": "up",
        "eth4": "down",
    },
    "router4": {
        "eth1": "up",
        "eth2": "down",
        "eth3": "down",
    },
    "pc1": {
        "eth1": "up",
    },
    "pc2": {
        "eth1": "up",
    },
    "pc3": {
        "eth1": "up",
    },
}

for host in hosts.values():
    for interface, state in ifstates[host.name].items():
        host.set_interface(interface, state)
