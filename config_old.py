# number for placeholder
p_number = '+79999config.py999999'
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
# HOST = '46.243.233.79' # This is the real IP address of the server (not to be used remotely)
PORT = 5000

# Database connection parameters
db_config = {
    'user': 'mike',        # MySQL username
    'password': '123456',  # MySQL password
    'host': 'mysql-db',   # Hostname of the MySQL container
    'port': 3306,            # Port number for MySQL
    'database': 'users'    # Name of the database you want to connect to
}