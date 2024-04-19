#!/usr/bin/python3
import socket

def check_server(address, port):
    # Create a socket object
    s = socket.socket()
    try:
        # Try to connect to the server
        s.connect((address, port))
        print(f"Server {address}:{port} is reachable.")
        # If connection is successful, return True
        return True
    except socket.error as e:
        # If connection fails, print the error and return False
        print(f"Server {address}:{port} is unreachable: {e}")
        return False
    finally:
        # Close the socket
        s.close()

# IP address and port of the server you want to monitor
server_ip = '9.0.0.2'
server_port = 80
# Check if the server is reachable
check_server(server_ip, server_port)
