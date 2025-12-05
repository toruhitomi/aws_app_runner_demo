# AWS App Runner Demo API

A demo REST API built with FastAPI, designed to be deployed on AWS App Runner.

## Features

- FastAPI-based REST API
- Health check endpoint for AWS App Runner
- Docker support for container-based deployment

## API Endpoints

- `GET /` - Welcome message
- `GET /health` - Health check endpoint
- `GET /docs` - Interactive API documentation (Swagger UI)

## Local Development

### Prerequisites

- Python 3.12+
- pip

### Installation

```bash
pip install -r requirements.txt
```

### Running the Application

```bash
uvicorn main:app --host 0.0.0.0 --port 8080
```

The API will be available at `http://localhost:8080`

## Docker

### Build

```bash
docker build -t aws-app-runner-demo .
```

### Run

```bash
docker run -p 8080:8080 aws-app-runner-demo
```

## AWS App Runner Deployment

This application is configured to run on AWS App Runner using the container-based deployment method.

1. Push your Docker image to Amazon ECR
2. Create an App Runner service pointing to your ECR repository
3. App Runner will use the health check endpoint at `/health` for service health monitoring

## License

Apache License 2.0
