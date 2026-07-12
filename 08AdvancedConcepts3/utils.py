from passlib.context import CryptContext

pwd_context = CryptContext(schemes=['bcrypt'], deprecated='auto')
fake_user_db={
  'johedoe':{
    'username':'johndoee',
    'hashed_password':pwd_context.hash('secret1234')

  }
}

def get_user(username:str):
  user=fake_user_db.get(username)
  return user


def verify_pass(plain_pass,hashed_pass):
  return pwd_context.verify(plain_pass,hashed_pass)