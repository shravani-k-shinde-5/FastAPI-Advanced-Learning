from fastapi import FastAPI, Depends



app = FastAPI()

def get_db():
    db = {'connection':'mock-connection'}
    try:
        yield db
    finally:
        db.close()

@app.get("/")
def home(db= Depends(get_db)):
    return {'db_status':db['connection']}