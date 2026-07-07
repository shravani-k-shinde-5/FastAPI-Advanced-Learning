from fastapi import FastAPI, Depends, HTTPException, status,form
from fastapi.security import OAuth2PasswordBearer

app = FastAPI()