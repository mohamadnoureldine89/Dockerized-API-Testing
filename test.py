import requests
import os

# Configuration
CONFIG = {
    'api_address': 'host.docker.internal', # shouldnt be localhost!!!!
    'api_port': 8000}

EXPECTED_STATUS = 200

# Helper function to send requests
def send_request(endpoint, params):
    url = f'http://{CONFIG["api_address"]}:{CONFIG["api_port"]}/{endpoint}'
    response = requests.get(url, params=params)
    return response

# Helper function to generate and log output
def generate_and_log_output(test_type, endpoint, username, password, status_code, additional_info=None):
    test_status = 'SUCCESS' if status_code == EXPECTED_STATUS else 'FAILURE'
    output = f'''
============================
    {test_type}
============================
request done at "{endpoint}"
| username = {username}
| password = {password}
expected result = {EXPECTED_STATUS}
actual result = {status_code}
==>  {test_status}
'''
    if additional_info:
        output += additional_info

    if os.environ.get('LOG') == 1:
        with open('/logs/api_test.log', 'a') as file:
            file.write(output)