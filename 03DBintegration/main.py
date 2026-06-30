from fastapi import FastAPI, HTTPException, Depends
from sqlalchemy.orm import Session
from typing import List
from database import Base
# Import your database elements, schemas, and crud operations
from database import engine, SessionLocal, Base
import schemas
import crud

# Create database tables
Base.metadata.create_all(bind=engine)

app = FastAPI()

# Dependency to get the database session
def get_DB():
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()

# Create employee
@app.post('/create', response_model=schemas.Employeeout)
async def create(emp: schemas.Employeecreate, db: Session = Depends(get_DB)):
    return crud.create_emp(db, emp)

# View all employees
@app.get('/view', response_model=List[schemas.Employeeout])
async def get_emp(db: Session = Depends(get_DB)):
    return crud.get_employee(db)

# View one employee by ID
@app.get('/view_one/{emp_id}', response_model=schemas.Employeeout)
async def get_emp1(emp_id: int, db: Session = Depends(get_DB)):
    employee = crud.get_employee(db, emp_id)
    if employee is None:
        raise HTTPException(status_code=404, detail="Employee not found")
    return employee


@app.put('/employee/{emp_id}',response_model=schemas.Employeeout)
def update(emp_id:int,employee:schemas.EmployeeUpdate):
    db_employee=crud.update_employee(db,emp_id,employee)
    if db_employee is None:
        raise HTTPException(status_code=404,details="employee not found")
    return db_employee

@app.delete('/employee{emp_id}',response_model=schemas.Employeeout)
def delete(emp_id:int,db:Session=Depends(get_DB)):
    employee =crud.delete_employee(db,emp_id)
    if employee is None:
        raise HTTPException(
            status_code=404,details='employee not found'
        )
    
    return employee
    

