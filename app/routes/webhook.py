from fastapi import APIRouter, Request, Header, HTTPException, Depends
from sqlalchemy.orm import Session
import hmac
import hashlib
import json

from app.database import get_db
from app.models import WebhookEvent
from app.config import settings

router = APIRouter()


def verify_signature(payload: bytes, signature: str):
    expected_signature = hmac.new(
        settings.WEBHOOK_SECRET.encode(),
        payload,
        hashlib.sha256
    ).hexdigest()

    if not hmac.compare_digest(expected_signature, signature):
        raise HTTPException(status_code=401, detail="Invalid signature")


@router.post("/webhook")
async def receive_webhook(
    request: Request,
    x_signature: str = Header(None),
    db: Session = Depends(get_db)
):
    body = await request.body()

    if not x_signature:
        raise HTTPException(status_code=400, detail="Missing signature")

    verify_signature(body, x_signature)

    data = json.loads(body)

    event = WebhookEvent(
    event_type=data.get("type"),
    payload=json.dumps(data)  # <-- convert dict to string
)


    db.add(event)
    db.commit()

    return {"status": "verified and stored"}
