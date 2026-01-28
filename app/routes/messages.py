# app/routes/messages.py
from fastapi import APIRouter, Depends
from sqlalchemy.orm import Session
from app.database import get_db
from app.models import Message

router = APIRouter()

@router.post("/messages")
def create_message(content: str, db: Session = Depends(get_db)):
    new_message = Message(content=content)
    db.add(new_message)
    db.commit()
    db.refresh(new_message)
    return {"status": "message stored", "id": new_message.id}

@router.get("/messages")
def get_messages(db: Session = Depends(get_db)):
    messages = db.query(Message).all()
    return [{"id": m.id, "content": m.content} for m in messages]
