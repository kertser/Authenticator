# number for placeholder
p_number = '+79999999999'
code = '123456'
token = 00000

# Everything is valid by default
phone_number_valid = True  # Valid format
phone_number_accepted = False  # Accepted by server
code_valid = False  # Valid format
code_accepted = False  # Accepted by server

# Server address:

#  HOST = '0.0.0.0'  # will be on the docker, remotely
server_HOST = '46.243.233.79'  # This is the real IP address of the server (not to be used remotely)
server_PORT = 5000  # Server port

server_url = f"http://{server_HOST}:{server_PORT}"