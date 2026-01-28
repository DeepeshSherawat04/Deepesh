import time
from fastapi import Request
from starlette.middleware.base import BaseHTTPMiddleware

# Dictionary to store metrics
metrics_data = {
    "total_requests": 0,
    "endpoints": {},  # track per-path metrics
}

class MetricsMiddleware(BaseHTTPMiddleware):
    async def dispatch(self, request: Request, call_next):
        start_time = time.time()
        response = await call_next(request)
        process_time = time.time() - start_time

        # Update total requests
        metrics_data["total_requests"] += 1

        # Update endpoint-specific metrics
        path = request.url.path
        if path not in metrics_data["endpoints"]:
            metrics_data["endpoints"][path] = {
                "requests": 0,
                "avg_response_time": 0,
                "status_codes": {}
            }

        endpoint_metrics = metrics_data["endpoints"][path]
        endpoint_metrics["requests"] += 1

        # Update average response time
        prev_avg = endpoint_metrics["avg_response_time"]
        endpoint_metrics["avg_response_time"] = (
            (prev_avg * (endpoint_metrics["requests"] - 1) + process_time) / endpoint_metrics["requests"]
        )

        # Update status code count
        status_code = str(response.status_code)
        if status_code not in endpoint_metrics["status_codes"]:
            endpoint_metrics["status_codes"][status_code] = 0
        endpoint_metrics["status_codes"][status_code] += 1

        return response
