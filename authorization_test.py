from test import send_request, generate_and_log_output

# Authorization Tests
users = [("bob", "builder"), ("alice", "wonderland")]
sentence = "Have a great day!"
test_type = "authorization_test"

for version in ['v1', 'v2']:
    for user, pwd in users:
        params = {'username': user, 'password': pwd, 'sentence': sentence}
        response = send_request(f'{version}/sentiment', params)
        generate_and_log_output(test_type, f'{version}/sentiment', user, pwd, response.status_code)
