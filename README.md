# Microservice Boilerplate Project

This project contains multiple microservices built using the FastAPI and Poetry boilerplate.

## Microservices

- `sample_microservice`: A simple microservice boilerplate for POC projects.

## Setup Instructions

1. **Clone the Repository**

   ```bash
   git clone https://github.com/yourusername/project_root.git
   cd project_root
   ```

2. **Build and Run with Docker Compose**

   ```bash
   docker-compose up --build
   ```

## Creating a New Microservice

To create a new microservice based on the boilerplate:

1. Copy the `sample_microservice` directory and rename it to your desired microservice name.
2. Update the project metadata in the `pyproject.toml` file.
3. Implement your microservice logic in the `app` directory.
4. Add the new microservice to the `docker-compose.yml` file.

Refer to the README file in each microservice directory for more details.
