from netmiko import ConnectHandler

device = {
    "device_type": "hp_comware",
    "host": "192.168.56.122",
    "username": "ssh_user",
    "password": "123456",
    "port": 22
}

# hosts = ["192.168.56.122"]
hosts = ["192.168.56.122","192.168.56.133"]

comm = ["ping 192.168.56.2"]

for i in range(len(hosts)):
    device["host"] = hosts[i]
    with ConnectHandler(**device) as conn:
        outs = conn.send_config_set(comm)
        print(outs)