from fastapi import FastAPI, Depends, HTTPException, status,form
from fastapi.security import OAuth2PasswordBearer

app = FastAPI()
oauth2_scheme = OAuth2PasswordBearer(tokenUrl="token")


@app.post("/token")
async def login(username: str = form(...), password: str = form(...)):
  if username == "admin" and password == "secret":
    return {"access_token": "fake-token", "token_type": "bearer"}
  raise HTTPException(status_code=status.HTTP_401_UNAUTHORIZED, detail="Invalid credentials")

def decode_token(token: str):
  if token == "valid-token":
    return {"username": "admin"}
  raise HTTPException(status_code=status.HTTP_401_UNAUTHORIZED, detail="Invalid token")


def get_current_user(token: str = Depends(oauth2_scheme)):
  return decode_token(token)

@app.get('/profile')
def read_profile(current_user: dict = Depends(get_current_user)):
  return {"username": current_user["username"]}
