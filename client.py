# This is a CLI client for the server. To run it, you need to have the server running.

import requests
import json
import config

# Define the server URL
server_url = config.server_url
# server_url = "http://localhost:5000" # local testing

# Example data for sending a phone number
phone_number_data = {
    "phone_number": "+972546490221"
}

# Example data for verifying a code
code_data = {
    "phone_number": "+972546490221", "password": "12345"
}

# Send a GET request to return a template
response = requests.get(f"{server_url}/get_template")
# decode the json response
if response.status_code == 200:
    template = json.loads(response.text)
    print(template)

# Send a POST request to check the phone number
response = requests.post(f"{server_url}/check_phone", json=phone_number_data)

# Check the response status code
if response.status_code == 200:
    print("Phone number found in the database.")
elif response.status_code == 404:
    print("Phone number NOT found in the database.")
else:
    print("Error:", response.status_code, response.text)

# Send a POST request to verify the code
response = requests.post(f"{server_url}/verify_code", json=code_data)

# Check the response status code
if response.status_code == 200:
    data = json.loads(response.text)
    token = data.get('token')
    print(f"Token: {token}")
elif response.status_code == 404:
    print("Code does not match.")
else:
    print("Error:", response.status_code, response.text)
