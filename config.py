# number for placeholder
p_number = '+79999999999'
code = '123456'
token = 00000
# Everything is valid by default
phone_number_valid = True  # Valid format
phone_number_accepted = False  # Accepted by server
code_valid = False  # Valid format
code_accepted = False  # Accepted by server

# Server address

# HOST = 'localhost'  # for local test only
HOST = '0.0.0.0'  # will be on the docker, remotely
# HOST = '46.243.232.144' # This is the real IP address of the server (not to be used remotely)
PORT = 5000

# Database connection parameters
db_config = {
    "host": "localhost",
    "user": "mike",
    "password": "123456",
    "database": "users"  # Replace with your database name
}