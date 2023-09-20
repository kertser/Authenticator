# Configuration file for the server

HOST = 'localhost'  # for local test only
# HOST = '0.0.0.0'  # will be on the docker, remotely
# HOST = '46.243.233.79' # This is the real IP address of the server (not to be used remotely)
PORT = 5000

server_url = f"http://{HOST}:{PORT}"

# Database configuration properties
db_config = {
    f"host": HOST,
    'port': 3306,
    'user': 'mike',
    'password': 'dovKh5dkt',
    'db': 'users',
    'charset': 'utf8mb4',
}