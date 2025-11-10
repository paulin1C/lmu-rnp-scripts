from ssh_helpers import hosts

bridge_name = "brr"

for host in hosts.values():
    if host.name in ["router1", "router2", "router3"]:
        host.run(f"ip link add name {bridge_name} type bridge")
        host.set_interface_up(bridge_name)
        for interface in [f"eth{n}" for n in [1, 2, 3, 4]]:
            host.run(f"ip addr flush dev {interface}")
            host.run(f"ip link set {interface} master {bridge_name}")
