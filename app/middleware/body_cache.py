from starlette.middleware.base import BaseHTTPMiddleware
from fastapi import Request

class BodyCacheMiddleware(BaseHTTPMiddleware):
    async def dispatch(self, request: Request, call_next):
        body = await request.body()

        # 🔴 THIS IS THE CRITICAL LINE
        request.state.body = body

        response = await call_next(request)
        return response
