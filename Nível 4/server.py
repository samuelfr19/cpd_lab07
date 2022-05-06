"""
 Implements a simple socket server

"""

import socket

# Define socket host and port
SERVER_HOST = '0.0.0.0'
SERVER_PORT = 8000

# Create socket
while True:
    server_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    server_socket.setsockopt(socket.SOL_SOCKET, socket.SO_REUSEADDR, 1)
    server_socket.bind((SERVER_HOST, SERVER_PORT))

    server_socket.listen(1)
    print('Listening on port %s ...' % SERVER_PORT)

    # Wait for client connections

    client_connection, client_address = server_socket.accept()

    # Print message from client
    msg = client_connection.recv(1024).decode()

    print('Received:', msg)

    if msg == "exit":
        server_socket.close()
        print("exiting ...")
        break

    print("returning message... " + msg)
    client_connection.send(msg.encode())

    # Close client connection
    client_connection.close()

    # Close socket
    server_socket.close()
