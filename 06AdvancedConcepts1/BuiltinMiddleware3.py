from fastapi import FastAPI, Request
from starlette.middleware.httpsredirect import  HTTPSRedirectMiddleware

app = FastAPI()
app.add_middleware(HTTPSRedirectMiddleware)