from fastapi import FastAPI, Depends, HTTPException
from fastapi.security import OAuth2PasswordBearer, OAuth2PasswordRequestForm
from auth import create_access_token, verify_access_token
from model import User, hashed_user
from utils import get_user, verify_pass

app = FastAPI()

oauth2_scheme = OAuth2PasswordBearer(tokenUrl='token')


@app.post('/token')
def login(form_data: OAuth2PasswordRequestForm = Depends()):
    user_dict = get_user(form_data.username)

    if not user_dict:
        raise HTTPException(
            status_code=404,
            detail="not found user"
        )

    if not verify_pass(form_data.password, user_dict['hashed_pass']):
        raise HTTPException(
            status_code=401,
            detail="invalid password"
        )

    access_token = create_access_token(
        data={'sub': form_data.username}
    )

    return {
        'access_token': access_token,
        'token_type': 'bearer'
    }


@app.get("/user")
def read_users(token: str = Depends(oauth2_scheme)):
    username = verify_access_token(token)
    return {'username': username}