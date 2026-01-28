from fastapi import APIRouter, Depends
from sqlalchemy.orm import Session
from sqlalchemy import func
from app.database import get_db  # use your existing DB session dependency
from app.models import Message  # import the ORM model

router = APIRouter()

@router.get("/stats")
def get_stats(db: Session = Depends(get_db)):
    total_messages = db.query(func.count(Message.id)).scalar()
    avg_length = db.query(func.avg(func.length(Message.content))).scalar()
    
    return {
        "total_messages": total_messages,
        "average_message_length": round(avg_length or 0, 2)
    }
