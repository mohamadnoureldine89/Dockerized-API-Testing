from test import send_request, generate_and_log_output

# Content Test
user = "alice"
pwd = "wonderland"
sentences = ["life is beautiful", "that sucks"]
versions = ['v1', 'v2']

for version in versions:
    for sentence in sentences:
        params = {'username': user, 'password': pwd, 'sentence': sentence}
        response = send_request(f'{version}/sentiment', params)
        score_info = f'\nsentence is {sentence}\nactual result = {response.json()["score"]}\n'
        generate_and_log_output(f'Content test {version.upper()}', f'{version}/sentiment', user, pwd, response.status_code, score_info)

