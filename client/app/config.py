# This is a config file for the Client App GUI

# Placeholders for the phone number, code and token - for UI
p_number = '+79999999999'
code = '123456'
token = 00000

# Everything is valid by default
phone_number_valid = True  # Valid format
phone_number_accepted = False  # Accepted by server
code_valid = False  # Valid format
code_accepted = False  # Accepted by server

# Server addresses:
#  HOST = '0.0.0.0'  # will be on the docker, remotely
server_HOST = '46.243.233.79'  # This is the real IP address of the server (not to be used remotely)
server_PORT = 5000  # Server port

# Server URL:
server_url = f"http://{server_HOST}:{server_PORT}"
