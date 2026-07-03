from fastapi import FastAPI, Request
from starlette.middleware.gizp import GZipMiddleware

app = FastAPI()
app.add_middleware(GZipMiddleware, minimum_size=1000)
