# Lyftr Backend

This is the backend for **Lyftr**, built with **FastAPI** and **SQLAlchemy**, containerized with **Docker**.  
You can find the project on GitHub: [https://github.com/DeepeshSherawat04/Deepesh](https://github.com/DeepeshSherawat04/Deepesh)

---

## Features

- FastAPI server with REST API endpoints
- SQLite database support via SQLAlchemy
- Logging middleware for incoming requests
- Metrics endpoint for monitoring usage
- Webhook endpoint with HMAC SHA256 signature verification
- Dockerized for easy deployment

---

## Requirements

- Python 3.11+
- Docker & Docker Compose
- FastAPI, Uvicorn, SQLAlchemy, python-dotenv

---

## Setup

### 1. Using Python locally

```bash
# Install dependencies
pip install -r requirements.txt

# Run the server
python -m uvicorn app.main:app --reload
2. Using Docker
# Build Docker image
docker build -t lyftr-backend .

# Run container
docker run -d -p 8000:8000 --name lyftr-api \
  -v ./app.db:/app/app.db \
  --env-file .env \
  lyftr-backend
Or using Docker Compose:

docker compose up --build
API Endpoints
Health
GET /health → Basic health check

GET /health/live → Liveness check ({"status":"alive"})

GET /health/ready → Readiness check ({"status":"ready"})

Messages
GET /messages → Get all messages

POST /messages?content=your_message → Store a new message

Webhook
POST /webhook

Requires JSON payload with a message field

Requires X-Signature header: HMAC SHA256 of the payload using WEBHOOK_SECRET from .env

Example:

curl -i -X POST http://localhost:8000/webhook \
  -H "Content-Type: application/json" \
  -H "X-Signature: <9c57a00c4f58ec368f6ecc287442be84e48d73966793ba60dd38e8f4493778b2>" \
  -d '{"message":"Hello"}'
Metrics & Stats
GET /metrics → Returns endpoint request counts, average response times, and status codes

GET /stats → Returns total messages and average message length

Environment Variables
Create a .env file in the project root:

DATABASE_URL=sqlite:///./app.db
WEBHOOK_SECRET=<b9e4136688dc4e4e8619a4bfdccfa8e9>
Docker Notes
Database persistence is enabled via volume: ./app.db:/app/app.db

Docker Compose restart: unless-stopped ensures the container auto-restarts

Remove the version: '3.9' line in docker-compose.yml if using Docker Compose V2

License
This project is open-source and free to use.