
from fastapi import FastAPI # type: ignore

app = FastAPI()


@app.get("/")
async def root():
    return {"message": "Hello World"}

@app.get("/about")
async def about():
    return {"message": "This is the about page"}


