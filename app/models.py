from sqlalchemy import Column, Integer, String, DateTime, create_engine
from sqlalchemy.orm import declarative_base, sessionmaker
from datetime import datetime
import json

DATABASE_URL = "sqlite:///./app.db"

Base = declarative_base()
engine = create_engine(DATABASE_URL, connect_args={"check_same_thread": False})
SessionLocal = sessionmaker(bind=engine, autoflush=False, autocommit=False)

# Messages table
class Message(Base):
    __tablename__ = "messages"
    id = Column(Integer, primary_key=True, index=True)
    content = Column(String, nullable=False)

# Webhook events table
class WebhookEvent(Base):
    __tablename__ = "webhook_events"
    id = Column(Integer, primary_key=True, index=True)
    event_type = Column(String, nullable=False)
    payload = Column(String, nullable=False)
    created_at = Column(DateTime, default=datetime.utcnow)

# Convert dict payload to JSON string automatically if needed
def webhook_payload_to_str(payload):
    if isinstance(payload, dict):
        return json.dumps(payload)
    return payload

# Initialize DB tables
def init_db():
    Base.metadata.create_all(bind=engine)
