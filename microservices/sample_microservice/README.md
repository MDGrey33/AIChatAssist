# Sample Microservice

A simple microservice boilerplate for POC projects using FastAPI and Poetry.

## Setup Instructions

### Prerequisites

- Python 3.12
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
