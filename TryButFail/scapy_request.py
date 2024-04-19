from scapy.all import IP, TCP, send, Raw

# Define source and destination IP addresses
src_ip = "127.18.0.1"
dst_ip = "172.18.0.3"

# Define source and destination ports
src_port = 12345  # Choose an unused port
dst_port = 80     # HTTP default port

# Craft IP packet with TCP layer
ip_packet = IP(src=src_ip, dst=dst_ip)
tcp_packet = TCP(sport=src_port, dport=dst_port, flags="S", seq=1000)

# HTTP request
http_request = (
    "GET / HTTP/1.1\r\n"
    "Host: example.com\r\n"
    "Connection: keep-alive\r\n"
    "\r\n"
)

# Combine packets
packet = ip_packet / tcp_packet / Raw(load=http_request)

# Send the packet
response = send(packet, verbose=False)
