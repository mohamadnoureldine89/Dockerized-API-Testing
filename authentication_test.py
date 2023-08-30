from test import send_request, generate_and_log_output

# Authentication Tests
auth_tests = [
    ('alice', 'wonderland'),
    ('bob', 'builder'),
    ('test_user', 'password2')
]

test_type = "authentication_test"

for username, password in auth_tests:
    params = {'username': username, 'password': password}
    response = send_request('permissions', params)
    generate_and_log_output(test_type, 'permissions', username, password, response.status_code)
