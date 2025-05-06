from netmiko import ConnectHandler

device = {
  "device_type":"hp_comware",
  # "device_type":"hp_comware_telnet",
  "host":"192.168.56.122",
  "username":"ssh_user",
  "password":"123456",
  "port":"22"
  # "port":"23"
}

comm = ["dis ip int b"]

with ConnectHandler(**device) as conn:
  outs = conn.send_config_set(comm)
  print(outs)