import netmiko


def read_config(file):

    with open(filename, 'r') as file:
        lines = file.readlines()
        host = lines[0].strip()
        user = lines[1].strip()
        pwd = lines[2].strip()
        connect_port = lines[3].strip()
        hidden = lines[4].strip()
        device_ios = lines[5].strip()
    return host, user, pwd, connect_port, device_ios, hidden


for i in range(1, 4):
    filename = f"router_config_{i}.txt"
    hostname, username, password, port, device_type, secret = read_config(filename)

    device = {
        "device_type": device_type,
        "host": hostname,
        "username": username,
        "password": password,
        "port": port,
        "secret": secret
    }

    connection = netmiko.ConnectHandler(**device)
    print(f"Connected to: {hostname}")

    connection.enable()

    ospf = connection.send_config_from_file("ospf_routing_protocol.txt")
    print(ospf)




