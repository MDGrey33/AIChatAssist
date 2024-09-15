# Sample Microservice

A simple microservice boilerplate for POC projects using FastAPI and Poetry.

## Setup Instructions

### Prerequisites

- Python 3.12
- Poetry
- Docker
- Git

### Installation

1. **Install Dependencies**

   ```bash
   poetry install
   ```

2. **Run the Application**

   ```bash
   poetry run uvicorn app.main:app --reload
   ```

3. **Build and Run with Docker**

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
