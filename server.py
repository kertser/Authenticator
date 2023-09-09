import socket
import json
import config
import warnings
import mysql.connector

# Kill all warnings
warnings.filterwarnings("ignore")

HOST = config.HOST
PORT = config.PORT


def get_record_by_phone_number(phone_number_to_find):
    """
    This function will retrieve a record from the "users" table by the phone number.
    :param phone_number_to_find: The phone number to find
    :return: The record
    """
    # Connect to the MySQL database

    connection = None
    try:
        connection = mysql.connector.connect(**config.db_config)

        if connection.is_connected():
            cursor = connection.cursor()

            # SQL query to check if the phone number exists in the "users" table
            query = "SELECT * FROM users WHERE phone_number = %s"
            cursor.execute(query, (phone_number_to_find,))

            # Get the result
            result = cursor.fetchone()

            return result

    except mysql.connector.Error as error:
        print("Error:", error)

    finally:
        if connection.is_connected():
            cursor.close()
            connection.close()


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

            """
            On connection, the client sends a JSON string with the phone number.
            If the client sends a JSON string with the phone number, the server checks if the phone number is in the list.
            If the phone number is in the list, the server sends a JSON string with the result of the operation and awaits
            for the client to send a JSON string with the code.
            If the client sends a JSON string with the code, the server checks if the code is correct.
            The assumption is that the client will send a JSON string with the phone number first, and then the code.
            """
            try:
                json_dict = json.loads(received_string)
                if 'phone_number' in json_dict:
                    phone_number = json_dict['phone_number']
                    print(f'Received phone number from client is: {phone_number}')

                    record = list(get_record_by_phone_number(phone_number))
                    if record is not None:  # Phone number is in list
                        print(f'Phone number is in list')

                        response_string = json.dumps({'result': True, 'message': '200'})  # correct number
                        conn.sendall(response_string.encode())
                    else:
                        response_string = json.dumps({'result': False, 'message': '100'})  # incorrect number
                        conn.sendall(response_string.encode())
                elif 'code' in json_dict:
                    code = json_dict['code'] # This is the code from the client
                    password = record[3].decode('utf-8') # This is the password
                    print(f'Received code from client is: {code}')

                    if code == password:
                        token = record[4].decode('utf-8')
                        response_string = json.dumps({'result': True, 'message': '200', 'token': token})
                        conn.sendall(response_string.encode())
                    else:
                        response_string = json.dumps({'result': False, 'message': '300'})  # incorrect code
                        conn.sendall(response_string.encode())

            except json.decoder.JSONDecodeError:
                print('Received data is not a valid JSON')
                continue

            conn.close()
