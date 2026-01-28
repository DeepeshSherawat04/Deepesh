import hmac, hashlib

body = b'{"message":"Hello"}'
secret = "YOUR_WEBHOOK_SECRET"   # EXACT value from .env

signature = hmac.new(
    secret.encode(),
    body,
    hashlib.sha256
).hexdigest()

print(signature)



# 9c57a00c4f58ec368f6ecc287442be84e48d73966793ba60dd38e8f4493778b2