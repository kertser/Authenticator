import socket
import json
import config
import warnings

# test values
test_phone_number = '+7123456789'
test_code = '1234'
test_token = 'AAABBB'

# Kill all warnings
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

            try:
                json_dict = json.loads(received_string)
                if 'phone_number' in json_dict:
                    phone_number = json_dict['phone_number']
                    print(f'Received phone number from client is: {phone_number}')
                    if phone_number == test_phone_number:
                        response_string = json.dumps({'result': True, 'message': '200'})  # correct number
                        conn.sendall(response_string.encode())
                    else:
                        response_string = json.dumps({'result': False, 'message': '100'})  # incorrect number
                        conn.sendall(response_string.encode())
                elif 'code' in json_dict:
                    code = json_dict['code']
                    print(f'Received code from client is: {code}')
                    if code == test_code:
                        response_string = json.dumps({'result': True, 'message': '200', 'token': test_token})
                        conn.sendall(response_string.encode())
                    else:
                        response_string = json.dumps({'result': False, 'message': '300'})  # incorrect code
                        conn.sendall(response_string.encode())

            except json.decoder.JSONDecodeError:
                print('Received data is not a valid JSON')
                continue

            conn.close()
