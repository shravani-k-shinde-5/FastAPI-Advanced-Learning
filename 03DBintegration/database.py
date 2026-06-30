#this file helps to setup db connection 


from sqlalchemy import create_engine
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import sessionmaker


SQLALCHEMY_DB_URL ="sqlite:///./test.db"

# Remove the extra space
engine = create_engine(
    SQLALCHEMY_DB_URL, connect_args={"check_same_thread": False}
)

SessionLocal =sessionmaker(bind=engine,autoflush=False,autocommit=False)
Base =declarative_base()





