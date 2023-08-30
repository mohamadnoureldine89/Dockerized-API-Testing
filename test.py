import requests
import os
import json

# Helper function to send requests
def send_request(endpoint, params):
    # Configuration
    CONFIG = {
        'api_address': 'fastapi', 
        'api_port': 8000}

    url = f'http://{CONFIG["api_address"]}:{CONFIG["api_port"]}/{endpoint}'
    
    try:
        response = requests.get(url, params=params)
        response.raise_for_status()
    except Exception as err:
        response = requests.Response()
        response.status_code = 500  # Set status code to 500 (Internal Server Error)
        response._content = str(err).encode()  # Set the content of the response to the error message
        response.score = 0

    return response

# Helper function to generate and log output
def generate_and_log_output(test_type, endpoint, username, password, status_code, additional_info=None):
    EXPECTED_STATUS = 200
    log_path = f'/{test_type}/logs'

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
        if not os.path.exists(log_path):
            os.makedirs(log_path)

        with open(os.path.join(log_path, 'api_test.log'), 'a') as file:
            file.write(output + '\n')



