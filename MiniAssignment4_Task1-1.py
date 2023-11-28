for i in range(1, 4):
    filename = f"router_config_{i}.txt"

    hostname = f"192.168.122.{i * 10}"
    username = "u1"
    password = "cisco"
    secret = "cisco"
    device_type = "cisco_ios"
    port = "22"

    with open(filename, 'w') as file:
        file.write(f"{hostname}\n")
        file.write(f"{username}\n")
        file.write(f"{password}\n")
        file.write(f"{port}\n")
        file.write(f"{secret}\n")
        file.write(f"{device_type}\n")

print(f"Router configurations created successfully")
