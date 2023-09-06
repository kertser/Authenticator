import socket
import json
import config

# Kill all warnings
import warnings

warnings.filterwarnings("ignore")

HOST = config.HOST
PORT = config.PORT

with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as server_socket:
    # Server sockets operation
    server_socket.bind((HOST, PORT))
    server_socket.listen()
    print(f'Server is listening on port {PORT}')
    while True:
        conn, addr = server_socket.accept()
        with conn:
            print(f'Connected by {addr}')
            data = conn.recv(1024)
            received_string = data.decode('utf-8', 'ignore')
            phone_number = received_string

            print(f'Received phone number from client is: {phone_number}')

            response_string = '200'

            conn.sendall(response_string.encode())
            conn.close()
