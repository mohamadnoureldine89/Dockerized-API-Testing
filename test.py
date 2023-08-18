import requests
import os
import json

# Helper function to send requests
def send_request(endpoint, params):
    # Configuration
    CONFIG = {
        'api_address': 'localhost', 
        'api_port': 8000}

    url = f'http://{CONFIG["api_address"]}:{CONFIG["api_port"]}/{endpoint}'
    response = requests.get(url, params=params)
    return response

# Helper function to generate and log output
def generate_and_log_output(test_type, endpoint, username, password, status_code, additional_info=None):
    EXPECTED_STATUS = 200

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
        with open('/app/logs/api_test.log', 'w') as file:
            file.write(output)

    
"""    with open('api_test.log', 'a') as file:
        file.write(output)"""


