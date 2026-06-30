from pydantic import BaseModel,EmailStr

class EmployeeBase(BaseModel):
  name:str
  email:EmailStr


class Employeecreate(EmployeeBase):
  pass

class EmployeeUpdate(EmployeeBase):
  pass

class Employeeout(EmployeeBase):
  id:int

  class Config:
    orm_mode =True