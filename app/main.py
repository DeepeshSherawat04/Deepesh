from fastapi import FastAPI
from fastapi import HTTPException, Depends
from sqlalchemy.orm import Session
from sqlalchemy import text

from app.routes import webhook, messages, stats
from app.models import init_db
from app.database import get_db
from app.middleware.metrics import MetricsMiddleware, metrics_data

# -------------------------------
# Initialize Database Tables
# -------------------------------
init_db()

# -------------------------------
# Create FastAPI App
# -------------------------------
app = FastAPI(title="Lyftr Backend Assignment")

# -------------------------------
# Register Routes
# -------------------------------
app.include_router(webhook.router)
app.include_router(messages.router)
app.include_router(stats.router)

# -------------------------------
# Add Metrics Middleware
# -------------------------------
app.add_middleware(MetricsMiddleware)

# -------------------------------
# Root Endpoint (Health Check)
# -------------------------------
@app.get("/")
def root():
    return {"status": "service running"}

# -------------------------------
# Health Endpoint
# -------------------------------
@app.get("/health")
def health_check(db: Session = Depends(get_db)):
    try:
        db.execute(text("SELECT 1"))
        db_status = "ok"
    except Exception as e:
        print("DB health check failed:", e)
        db_status = "failed"

    status = {"server": "ok", "database": db_status}
    if db_status != "ok":
        raise HTTPException(status_code=500, detail=status)
    return status

# -------------------------------
# Metrics Endpoint
# -------------------------------
@app.get("/metrics")
def get_metrics():
    return metrics_data
