import time
import logging
from fastapi import Request
from starlette.middleware.base import BaseHTTPMiddleware

# Configure Python logging
logging.basicConfig(
    level=logging.INFO,
    format="%(asctime)s - %(levelname)s - %(message)s",
)

class LoggingMiddleware(BaseHTTPMiddleware):
    async def dispatch(self, request: Request, call_next):
        start_time = time.time()

        # Log incoming request
        logging.info(f"Incoming request: {request.method} {request.url}")

        response = await call_next(request)

        process_time = time.time() - start_time
        logging.info(
            f"Response: {request.method} {request.url} - Status {response.status_code} - {process_time:.3f}s"
        )

        return response
