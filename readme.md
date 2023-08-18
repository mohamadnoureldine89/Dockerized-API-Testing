# Project Title: Dockerized API Testing

- This project contains a set of scripts that are used to test different aspects of a FastAPI server.
- The tests include authentication, authorization, and content tests. 
- The tests are run in Docker containers, and the results are logged to a logs file saved in a Docker volume.

## Project Structure

The project contains the following files:

- test.py: Python script containing helper functions for sending requests and generating logs.
- authentication_test.py: Python script for performing authentication tests.
- authorization_test.py: Python script for performing authorization tests.
- content_test.py: Python script for performing content tests.
- Dockerfile_authentication: Dockerfile for running authentication tests.
- Dockerfile_authorization: Dockerfile for running authorization tests.
- Dockerfile_content: Dockerfile for running content tests.
- docker-compose.yaml: Docker Compose file for running all tests.

## How to Run

- Run the Docker Compose file to start all the tests.
- Check the logs in the /app/logs directory in each container for the test results.

## Note

The scripts are set up to test a FastAPI server running on localhost:8000. Make sure the server is up and running before starting the tests.