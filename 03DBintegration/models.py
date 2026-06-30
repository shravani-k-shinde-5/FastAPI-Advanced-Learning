from sqlalchemy import Column,Integer,String
from database import Base

class Employee(Base):#Database table model
  """
  Because it inherits from Base, SQLAlchemy understands:

 This is not a normal Python class
 This should become a database table
"""
  __tablename__='employees'
  id=Column(Integer,primary_key=True,index=True)
  name =Column(String,index=True)
  email =Column(String,unique=True,index=True)

  