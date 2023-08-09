from test import send_request, generate_and_log_output

# Authorization Tests
users = [("bob", "builder"), ("alice", "wonderland")]
sentence = "Have a great day!"
for version in ['v1', 'v2']:
    for user, pwd in users:
        params = {'username': user, 'password': pwd, 'sentence': sentence}
        response = send_request(f'{version}/sentiment', params)
        generate_and_log_output('Authorization test', f'{version}/sentiment', user, pwd, response.status_code)
