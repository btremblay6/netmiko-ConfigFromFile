filename = "ospf_routing_protocol.txt"

with open(filename, 'w') as file:
    file.write("router ospf 1\n")
    file.write("net 0.0.0.0 0.0.0.0 area 0\n")
    file.write("distance 110\n")
    file.write("default-information originate")

print("OSPF configuration Completed successfully")
