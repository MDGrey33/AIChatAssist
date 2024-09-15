#!/bin/bash

# Navigate to the microservice directory
cd microservices/sample_microservice

# Set up the environment using Poetry
poetry install

# Run the tests using Poetry
poetry run pytest
