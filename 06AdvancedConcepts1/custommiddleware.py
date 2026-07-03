from fastapi import FastAPI, Request
from starlette.middleware.base import BaseHTTPMiddleware
import time

app = FastAPI()


class LoggingMiddleware(BaseHTTPMiddleware):

    async def dispatch(self, request: Request, call_next):

        start_time = time.time()

        print(f"Request: {request.method} {request.url}")

        response = await call_next(request)

        process_time = time.time() - start_time

        print(f"Completed in {process_time:.4f} seconds")

        return response


app.add_middleware(LoggingMiddleware)


@app.get("/")
async def home():
    return {"message": "Hello World"}