from fastapi import APIRouter, Request, Header, HTTPException, Depends
from sqlalchemy.orm import Session
import hmac, hashlib, json

from app.database import get_db
from app.models import WebhookEvent
from app.config import settings

router = APIRouter()


def verify_signature(payload: bytes, signature: str):
    key = settings.WEBHOOK_SECRET.encode("utf-8")
    expected = hmac.new(key, payload, hashlib.sha256).hexdigest()

    print("---- SIGNATURE DEBUG ----")
    print("PAYLOAD BYTES:", payload)
    print("PAYLOAD HEX:", payload.hex())
    print("SECRET:", settings.WEBHOOK_SECRET)
    print("EXPECTED:", expected)
    print("RECEIVED:", signature)
    print("-------------------------")

    if not hmac.compare_digest(expected, signature):
        raise HTTPException(status_code=401, detail="Invalid signature")


@router.post("/webhook")
async def receive_webhook(
    request: Request,
    x_signature: str = Header(...),
    db: Session = Depends(get_db)
):
    body: bytes = request.state.body  # ✅ now guaranteed

    verify_signature(body, x_signature)

    data = json.loads(body.decode("utf-8"))

    event = WebhookEvent(
        event_type=data.get("type"),
        payload=json.dumps(data)
    )

    db.add(event)
    db.commit()

    return {"status": "verified and stored"}
