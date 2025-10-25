This is a collection of scripts to help me interact with the hosts of a [university seminar](https://www.ifi.lmu.de/nm/de/lehre/wintersemester-2025-26/praktikum_rnp.html).

## Prerequisites
- python3
- connection to the vm-host with ``ssh rnp-cip``

### ``.ssh/config`` example
```
Host cip
        Hostname remote.cip.ifi.lmu.de
        User your_cip_username
        IdentityFile path/to/your/key/for/cip-pool

Host rnp-cip
        ProxyJump cip
        Hostname 10.153.211.195  # use the ip of your vm host; dns isn't reliable on the cip servers
        User rnp
        IdentityFile path/to/your/key/for/vm-host
```
