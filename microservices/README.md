# **Microservice Boilerplate with FastAPI and Poetry**

This guide provides a step-by-step approach to setting up a simple microservice boilerplate using **FastAPI** and **Poetry**. It is tailored for proof-of-concept (POC) projects and focuses on simplicity, avoiding production-level complexities like authentication or authorization. The boilerplate is designed to be reused for creating multiple microservices within the same repository, adhering to Python naming conventions.

---

## **Table of Contents**

- [**Microservice Boilerplate with FastAPI and Poetry**](#microservice-boilerplate-with-fastapi-and-poetry)
  - [**Table of Contents**](#table-of-contents)
  - [**Introduction**](#introduction)
  - [**Prerequisites**](#prerequisites)
  - [**Project Structure**](#project-structure)
  - [**Setting Up the Boilerplate**](#setting-up-the-boilerplate)
    - [**1. Create Project Directory**](#1-create-project-directory)
    - [**2. Initialize Poetry Project**](#2-initialize-poetry-project)
    - [**3. Define Application Code**](#3-define-application-code)
      - [**main.py**](#mainpy)
      - [**routes.py**](#routespy)
    - [**4. Configure Dependencies**](#4-configure-dependencies)
    - [**5. Create Dockerfile**](#5-create-dockerfile)
    - [**6. Write Tests**](#6-write-tests)
  - [**Using the Boilerplate to Create a New Microservice**](#using-the-boilerplate-to-create-a-new-microservice)
    - [**1. Copy the Boilerplate**](#1-copy-the-boilerplate)
    - [**2. Update Project Metadata**](#2-update-project-metadata)
    - [**3. Implement Service Logic**](#3-implement-service-logic)
    - [**4. Adjust Dependencies**](#4-adjust-dependencies)
    - [**5. Build and Run the Service**](#5-build-and-run-the-service)
    - [**6. Update Pre-commit Configuration**](#6-update-pre-commit-configuration)
  - [**Best Practices**](#best-practices)
  - [**Conclusion**](#conclusion)
  - [**Appendix: Full Code Listings**](#appendix-full-code-listings)
    - [**app/main.py**](#appmainpy)
    - [**app/routes.py**](#approutespy)
    - [**Dockerfile**](#dockerfile)
    - [**pyproject.toml**](#pyprojecttoml)
    - [**tests/test\_main.py**](#teststest_mainpy)
    - [**.gitignore**](#gitignore)
    - [**README.md**](#readmemd)
    - [Testing](#testing)
    - [API Endpoints](#api-endpoints)
  - [**Using Docker Compose for Multiple Microservices**](#using-docker-compose-for-multiple-microservices)
  - [**Final Notes**](#final-notes)

---

## **Introduction**

Creating microservices for POC projects requires a balance between simplicity and functionality. This guide provides a straightforward boilerplate using **FastAPI** and **Poetry**, enabling you to quickly set up microservices without the overhead of production features like authentication, authorization, or complex error handling. All microservices will reside within the same Git repository for easier management.

---

## **Prerequisites**

Ensure you have the following installed:

- **Python 3.7+**
- **Poetry**
- **Docker**
- **Git** (optional, for version control)

---

## **Project Structure**

```
project_root/
├── microservices/
│   ├── sample_microservice/
│   │   ├── app/
│   │   │   ├── __init__.py
│   │   │   ├── main.py
│   │   │   └── routes.py
│   │   ├── tests/
│   │   │   └── test_main.py
│   │   ├── Dockerfile
│   │   ├── pyproject.toml
│   │   ├── poetry.lock
│   │   └── README.md
│   └── ... (other microservices)
├── docker-compose.yml
├── .gitignore
└── README.md
```

- **project_root/**: Root directory of your project.
- **microservices/**: Contains all microservices.
- **sample_microservice/**: Directory for a microservice (using underscores as per Python conventions).
  - **app/**: Contains the application code.
    - **\_\_init\_\_.py**: Marks the directory as a Python package.
    - **main.py**: Entry point of the application where the FastAPI app is instantiated.
    - **routes.py**: Defines API endpoints.
  - **tests/**: Contains test cases.
    - **test_main.py**: Test suite for the application.
  - **Dockerfile**: Configuration for Docker image.
  - **pyproject.toml**: Contains project metadata and dependencies (managed by Poetry).
  - **poetry.lock**: Locks the exact versions of dependencies.
  - **README.md**: Documentation for the microservice.
- **docker-compose.yml**: Orchestrates all microservices.
- **.gitignore**: Specifies files and directories to ignore in version control.
- **README.md**: Documentation for the overall project.

---

## **Setting Up the Boilerplate**

### **1. Create Project Directory**

1. **Navigate to Your Project Root:**

   ```bash
   mkdir project_root
   cd project_root
   ```

2. **Create Microservices Directory:**

   ```bash
   mkdir microservices
   cd microservices
   ```

3. **Create a Sample Microservice Directory:**

   ```bash
   mkdir sample_microservice
   cd sample_microservice
   ```

### **2. Initialize Poetry Project**

Initialize a new Poetry project within the microservice directory:

```bash
poetry init
```

- Follow the prompts to set up the project metadata (name, version, description, etc.).
- Use underscores in the package name to adhere to Python naming conventions (e.g., `sample_microservice`).

### **3. Define Application Code**

#### **main.py**

Create `app/main.py` and add the following code:

```python
from fastapi import FastAPI
from app.routes import router

app = FastAPI()

app.include_router(router)
```

#### **routes.py**

Create `app/routes.py` and define your API endpoints:

```python
from fastapi import APIRouter

router = APIRouter()

@router.get("/health")
async def health_check():
    return {"status": "healthy"}
```

- **Note:** Use underscores in file names and variable names to follow Python conventions.

### **4. Configure Dependencies**

Add the necessary dependencies using Poetry:

```bash
poetry add fastapi uvicorn
```

- This updates the `pyproject.toml` file with the specified dependencies.

### **5. Create Dockerfile**

Create a `Dockerfile` in the root of your microservice directory:

```dockerfile
FROM python:3.9-slim

# Set work directory
WORKDIR /app

# Install Poetry
RUN pip install poetry

# Copy pyproject.toml and poetry.lock
COPY pyproject.toml poetry.lock ./

# Install dependencies
RUN poetry config virtualenvs.create false \
    && poetry install --no-dev --no-interaction --no-ansi

# Copy the application code
COPY . .

# Expose port
EXPOSE 8000

# Command to run the application
CMD ["poetry", "run", "uvicorn", "app.main:app", "--host", "0.0.0.0", "--port", "8000"]
```

### **6. Write Tests**

Create a `tests/` directory and add test cases.

**tests/test_main.py**

```python
from fastapi.testclient import TestClient
from app.main import app

client = TestClient(app)

def test_health_check():
    response = client.get("/health")
    assert response.status_code == 200
    assert response.json() == {"status": "healthy"}
```

---

## **Using the Boilerplate to Create a New Microservice**

### **1. Copy the Boilerplate**

From the `microservices/` directory, copy the boilerplate to create a new microservice:

```bash
cd project_root/microservices/
cp -r sample_microservice new_microservice
```

- Use underscores in the directory name (`new_microservice`) to follow Python conventions.

### **2. Update Project Metadata**

Update the project metadata in `pyproject.toml` of the new microservice:

```toml
[tool.poetry]
name = "new_microservice"
version = "0.1.0"
description = "Description of your new microservice."
authors = ["Your Name <you@example.com>"]
```

- Ensure the `name` uses underscores.

### **3. Implement Service Logic**

Modify `app/routes.py` and other files to implement the functionality specific to your new microservice.

- Use Python naming conventions for variables, functions, and file names.

### **4. Adjust Dependencies**

Add or remove dependencies using Poetry:

```bash
poetry add requests
poetry remove unnecessary_dependency
```

- This keeps your `pyproject.toml` and `poetry.lock` files up to date.

### **5. Build and Run the Service**

**Building the Docker Image:**

From the microservice directory:

```bash
docker build -t new_microservice:latest .
```

**Running the Docker Container:**

```bash
docker run -p 8000:8000 new_microservice:latest
```

- Map the container's port 8000 to your host machine's port 8000.
- Adjust the port numbers as needed if running multiple services.

### **6. Update Pre-commit Configuration**

When adding a new microservice to the project, it's important to update the pre-commit configuration to ensure that the tests for the new microservice are run as part of the pre-commit checks.

To do this, follow these steps:

1. Open the `.pre-commit-config.yaml` file in the project root.

2. Locate the `repos` section and find the `local` repository configuration.

3. Add a new hook for the new microservice, following the pattern of the existing hooks. For example:

   ```yaml
   - repo: local
     hooks:
       # ...existing hooks...

       - id: pytest-new-microservice
         name: pytest-new-microservice
         entry: bash microservices/new_microservice/run_tests.sh
         language: system
         types: [python]
         files: ^microservices/new_microservice/tests/
   ```

   - Replace `new_microservice` with the actual name of your new microservice directory.
   - Adjust the `entry` command to match the test script location and name for your new microservice.

4. Save the changes to the `.pre-commit-config.yaml` file.

By adding this new hook, pre-commit will now run the tests for your new microservice whenever you commit changes that affect the files within the `microservices/new_microservice/tests/` directory.

Remember to create a `run_tests.sh` script (or equivalent) within your new microservice directory to execute the tests using the appropriate command (e.g., `poetry run pytest`).

Updating the pre-commit configuration ensures that the tests for all microservices, including the newly added one, are run consistently as part of the pre-commit checks, helping maintain code quality and catch potential issues early in the development process.

---

## **Best Practices**

- **Python Naming Conventions:**

  - Use **lowercase with underscores** for module and package names (e.g., `new_microservice`).
  - Use **snake_case** for variables and function names.
  - Use **CapWords** (PascalCase) for class names.

- **Environment Variables:**

  - For POC projects, you can hard-code configurations or use a `.env` file.
  - Be cautious not to commit sensitive information if using version control.

- **Dependency Management:**

  - Keep dependencies minimal and only include what is necessary.
  - Regularly update dependencies to their latest compatible versions.

- **Code Organization:**

  - Separate routes, models, and utility functions into different modules for clarity.
  - Use `__init__.py` files to make directories recognizable as Python packages.

- **Testing:**

  - Write simple tests to verify the basic functionality of your microservice.
  - Use `pytest` or `unittest` frameworks for testing.

- **Version Control:**

  - Use a single Git repository for all microservices.
  - Add a `.gitignore` file to exclude unnecessary files from version control.

- **Documentation:**

  - Maintain a `README.md` with setup instructions and API documentation for each microservice.
  - Document any assumptions or limitations in your POC.

---

## **Conclusion**

This boilerplate provides a simple and effective starting point for developing microservices in a POC environment. By adhering to Python naming conventions and keeping the setup minimal, you can focus on implementing your application's core functionality without unnecessary complexity.

---

## **Appendix: Full Code Listings**

### **app/main.py**

```python
from fastapi import FastAPI
from app.routes import router

app = FastAPI()

app.include_router(router)
```

### **app/routes.py**

```python
from fastapi import APIRouter

router = APIRouter()

@router.get("/health")
async def health_check():
    return {"status": "healthy"}
```

### **Dockerfile**

```dockerfile
FROM python:3.9-slim

# Set work directory
WORKDIR /app

# Install Poetry
RUN pip install poetry

# Copy pyproject.toml and poetry.lock
COPY pyproject.toml poetry.lock ./

# Install dependencies
RUN poetry config virtualenvs.create false \
    && poetry install --no-dev --no-interaction --no-ansi

# Copy the application code
COPY . .

# Expose port
EXPOSE 8000

# Command to run the application
CMD ["poetry", "run", "uvicorn", "app.main:app", "--host", "0.0.0.0", "--port", "8000"]
```

### **pyproject.toml**

```toml
[tool.poetry]
name = "sample_microservice"
version = "0.1.0"
description = "A simple microservice boilerplate for POC projects."
authors = ["Your Name <you@example.com>"]

[tool.poetry.dependencies]
python = "^3.9"
fastapi = "^0.70.0"
uvicorn = "^0.15.0"

[tool.poetry.dev-dependencies]
pytest = "^6.2.5"
pytest-asyncio = "^0.15.1"

[build-system]
requires = ["poetry-core>=1.0.0"]
build-backend = "poetry.core.masonry.api"
```

- Ensure the `name` in `pyproject.toml` uses underscores.

### **tests/test_main.py**

```python
from fastapi.testclient import TestClient
from app.main import app

client = TestClient(app)

def test_health_check():
    response = client.get("/health")
    assert response.status_code == 200
    assert response.json() == {"status": "healthy"}
```

### **.gitignore**

```
# Python
__pycache__/
*.py[cod]
*.so
*.egg
*.egg-info/
dist/
build/

# Virtual Environments
venv/
ENV/
env/

# Poetry
poetry.lock

# Pytest cache
.cache/

# VS Code
.vscode/

# Environment Variables
.env
```

### **README.md**

```markdown
# Sample Microservice

A simple microservice boilerplate for POC projects using FastAPI and Poetry.

## Setup Instructions

### Prerequisites

- Python 3.9+
- Poetry
- Docker
- Git

### Installation

1. **Clone the Repository**

   ```bash
   git clone https://github.com/yourusername/project_root.git
   cd project_root/microservices/sample_microservice
   ```

2. **Install Dependencies**

   ```bash
   poetry install
   ```

3. **Run the Application**

   ```bash
   poetry run uvicorn app.main:app --reload
   ```

4. **Build and Run with Docker**

   ```bash
   docker build -t sample_microservice:latest .
   docker run -p 8000:8000 sample_microservice:latest
   ```

### Testing

```bash
poetry run pytest
```

### API Endpoints

- `GET /health`: Health check endpoint.

---

**Use this guide as a foundation to quickly set up new microservices with a consistent structure and naming conventions, facilitating easier collaboration and maintenance within a single repository.**

---

## **Using Docker Compose for Multiple Microservices**

In the project root, you can use a `docker-compose.yml` file to orchestrate all your microservices.

**docker-compose.yml**

```yaml
version: '3.8'

services:
  sample_microservice:
    build: ./microservices/sample_microservice
    ports:
      - "8000:8000"

  new_microservice:
    build: ./microservices/new_microservice
    ports:
      - "8001:8000"

  # Add other microservices here
```

- Adjust the port mappings to avoid conflicts.
- Use the service names (with underscores) consistently.

**To run all services:**

```bash
docker-compose up --build
```

---

## **Final Notes**

- **Consistency:** Adhering to Python naming conventions (using underscores) helps maintain consistency and readability across your codebase.
- **Simplicity:** Focus on implementing core features relevant to your POC without adding unnecessary complexities.
- **Scalability:** While this setup is ideal for POC projects, consider additional tools and practices (like authentication, error handling, and logging) for production-level applications.

Feel free to customize and extend this boilerplate to suit the specific needs of your project. Happy coding!
