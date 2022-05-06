"""
 Implements a simple socket client

"""

import socket


# Define socket host and port
SERVER_HOST = '127.0.0.1'
SERVER_PORT = 7000

# Create socket
client_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

# Connect to server
client_socket.connect((SERVER_HOST, SERVER_PORT))


# Send message
# client_socket.sendall("Hello from the client application!".encode())

msg = input("> ")
client_socket.send(msg.encode())

# Close socket
client_socket.close()