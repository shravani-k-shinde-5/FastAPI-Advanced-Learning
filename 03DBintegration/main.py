from fastapi import FastAPI, HTTPException, Depends
from sqlalchemy.orm import Session
from typing import List

from database import engine, SessionLocal, Base
import schemas
import crud

# Create tables
Base.metadata.create_all(bind=engine)

app = FastAPI()

# Dependency

"""

"""
def get_DB():
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()


# CREATE
@app.post('/create', response_model=schemas.EmployeeOut)
def create(emp: schemas.EmployeeCreate, db: Session = Depends(get_DB)):
    return crud.create_emp(db, emp)


# READ ALL
@app.get('/view', response_model=List[schemas.EmployeeOut])
def get_emp(db: Session = Depends(get_DB)):
    return crud.get_employees(db)


# READ ONE
@app.get('/view_one/{emp_id}', response_model=schemas.EmployeeOut)
def get_emp1(emp_id: int, db: Session = Depends(get_DB)):
    employee = crud.get_employee(db, emp_id)
    if employee is None:
        raise HTTPException(status_code=404, detail="Employee not found")
    return employee


# UPDATE
@app.put('/employee/{emp_id}', response_model=schemas.EmployeeOut)
def update(emp_id: int, employee: schemas.EmployeeUpdate, db: Session = Depends(get_DB)):
    db_employee = crud.update_employee(db, emp_id, employee)

    if db_employee is None:
        raise HTTPException(status_code=404, detail="Employee not found")

    return db_employee


# DELETE
@app.delete('/employee/{emp_id}', response_model=schemas.EmployeeOut)
def delete(emp_id: int, db: Session = Depends(get_DB)):
    employee = crud.delete_employee(db, emp_id)

    if employee is None:
        raise HTTPException(status_code=404, detail="Employee not found")

    return employee