#!/bin/bash

# Get the directory of the current script
SCRIPT_DIR="$(cd "$(dirname "${BASH_SOURCE[0]}")" && pwd)"

# Navigate to the microservice directory
cd "$SCRIPT_DIR"

# Set up the environment using Poetry
poetry install

# Run the tests using Poetry
poetry run pytest
