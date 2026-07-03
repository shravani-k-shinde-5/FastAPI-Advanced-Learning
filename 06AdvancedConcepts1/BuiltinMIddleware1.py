from fastapi import FastAPI, Request
from fastapi.middleware.cors import CORSMiddleware

app = FastAPI()

app.add_middleware(
    CORSMiddleware,
    allow_origins=['https://example.com','https://another-example.com','https://localhost:3000'],  
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
    
)

#define endpoints

@app.get("/")
async def read_root():
    return {"message": "Hello, World!"}
