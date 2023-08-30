from test import send_request, generate_and_log_output
import json
import requests

# Content Test
user = "alice"
pwd = "wonderland"
sentences = ["life is beautiful", "that sucks"]
versions = ['v1', 'v2']

test_type = "content_test"

for version in versions:
    for sentence in sentences:
        params = {'username': user, 'password': pwd, 'sentence': sentence}
        response = send_request(f'{version}/sentiment', params)
        score = response.json()["score"]
        score_info = f'\nsentence is {sentence}\nactual result = {score}\n'
        generate_and_log_output(test_type, f'{version}/sentiment', user, pwd, response.status_code, score_info)

