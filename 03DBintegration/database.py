#this file helps to setup db connection 


from sqlalchemy import create_engine
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import sessionmaker


SQLALCHEMY_DB_URL ="sqlite:///./test.db"


engine = create_engine(
    SQLALCHEMY_DB_URL, connect_args={"check_same_thread": False}
)

#if want to connect mysql which runs on server we use 
"""SQLALCHEMY_DB_URL = "mysql+pymysql://root:@localhost/student_db"

engine = create_engine(SQLALCHEMY_DB_URL)


mysql+pymysql://root:1234@localhost/student_db
│      │             │        │             │
│      │             │        │            └── Database name
│      │             │         └──────────── MySQL server address
│      │             └───────────────── Password
│      └──────────────────────────── Python driver
└────────────────────────────────── Database type
"""


"""every insert,delete,update ,selct i.e CRUD operation are not directly performed by python session performs this operations Python
 ↓
Session
 ↓
Database

"""
SessionLocal =sessionmaker(bind=engine,autoflush=False,autocommit=False)

"""this base is object of declarative_base() which helps sqlachemy to identify which classes are database tables as we declare each tables as class.So that  table (classes) get inherited from this base ."""

Base =declarative_base()


