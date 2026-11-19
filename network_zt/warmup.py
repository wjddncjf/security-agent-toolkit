PORTS = {80: "HTTP", 443: "HTTPS", 53: "DNS"}

print(PORTS[443])
print(PORTS.get(3389, "모름"))

flags = ["SYN", "ACK"]
print("SYN" in flags)   # True
print(flags == "SYN")   # False - 리스트와 글자는 같을 수 없다

packet = {"src_port": 51234, "dst_port": 443, "flags": ["SYN", "ACK"]}
print("ACK" in packet["flags"])
print(packet["flags"] == "ACK")
print(packet["dst_port"])