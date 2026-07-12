from pydantic import BaseModel

class User(BaseModel):
  user:str
  password:str



class hashed_user(User):
  hashed_pass :str