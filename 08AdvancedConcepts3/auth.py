from datetime import datetime, timedelta, timezone
from authlib.jose import JoseError,jwt
from fastapi import Depends, HTTPException, status


SECRET_KEY = 'mysecretkey'
ALGORITHM = 'HS256'
ACCESS_TOKEN_EXPIRE_MINUTES = 30

def create_access_token(data:dict):
  header = {"alg": ALGORITHM}
  expire = datetime.now(timezone.utc) + timedelta(minutes=ACCESS_TOKEN_EXPIRE_MINUTES)
  payload = data.copy()
  payload.update({"exp": expire})
  return jwt.encode(header, payload, SECRET_KEY)


def verify_access_token(token:str):
  try:
    claims = jwt.decode(token, SECRET_KEY)
    claims.validate()
    username = claims.get("username")
    if username is None:
      raise HTTPException(
        status_code=status.HTTP_401_UNAUTHORIZED,
        detail="Invalid token"
      )
  except JoseError:
    raise HTTPException(
      status_code=status.HTTP_401_UNAUTHORIZED,
      detail="Invalid token"
    )