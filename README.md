# Lyftr Backend

This is the backend for **Lyftr**, built with **FastAPI** and **SQLAlchemy**, containerized with **Docker**.

## Features
- FastAPI server with REST API endpoints
- SQLite/PostgreSQL database support via SQLAlchemy
- Logging middleware for incoming requests
- Metrics endpoint for monitoring
- Dockerized for easy deployment

## Requirements
- Python 3.11+
- Docker (for containerization)
- FastAPI, Uvicorn, SQLAlchemy, python-dotenv

## Setup

### Using Python locally
```bash
# Install dependencies
pip install -r requirements.txt

# Run the server
python -m uvicorn app.main:app --reload
Using Docker
# Build Docker image
docker build -t lyftr-backend .

# Run container
docker run -d -p 8000:8000 --name lyftr-app lyftr-backend
API Endpoints
GET /health → Server & database health check

POST /messages?content=your_message → Store a message

GET /messages → Get all messages

GET /metrics → Metrics for monitoring

License
This project is open-source and free to use.


---

### **2️⃣ Create a `.gitignore`**
Also, create a `.gitignore` in the same folder:

```gitignore
# Python
__pycache__/
*.py[cod]
*.env
*.sqlite3

# VS Code
.vscode/

# Docker
*.log
*.pid
*.pyc
*.pyo
*.pyd
env/
venv/
build/
dist/
*.egg-info/
.DS_Store