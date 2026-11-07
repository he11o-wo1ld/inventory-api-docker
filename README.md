# Inventory API - Docker Assignment

A simple Inventory Management REST API built using Python
and FastAPI, containerized using Docker.

## Technologies

- Python 3.12
- FastAPI
- Uvicorn
- Docker

## Project Structure

inventory-api-docker/
│
├── main.py
├── requirements.txt
├── Dockerfile
├── .dockerignore
└── README.md

## API Endpoints

| Method | Endpoint | Description |
|--------|----------|-------------|
| GET | / | Welcome message |
| GET | /health | Health check |
| GET | /items | Get all inventory items |
| GET | /items/{id} | Get item by ID |
| POST | /items | Create a new item |

## Build Docker Image

docker build -t inventory-api:1.0 .

## Run Container A

docker run -d --name inv-a -p 8081:5000 inventory-api:1.0

## Run Container B

docker run -d --name inv-b -p 8082:5000 inventory-api:1.0

## Check Running Containers

docker ps

## Test API

Container A:
http://localhost:8081/items

Container B:
http://localhost:8082/items

Swagger Documentation:
http://localhost:8081/docs

## Stop Container B

docker stop inv-b

## View All Containers

docker ps -a

## Docker Concepts

- Dockerfile: Instructions to build an image.
- Docker Image: Packaged application and dependencies.
- Docker Container: Running instance of an image.
- Port Mapping: Maps host ports to container ports.

Both containers use internal port 5000 but different host
ports (8081 and 8082), allowing them to run simultaneously.# inventory-api-docker
