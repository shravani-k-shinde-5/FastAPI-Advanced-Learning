from fastapi import FastAPI, Path, HTTPException, Query
import json
from fastapi.responses import JSONResponse
from .models import PatientUpdate,patient


app = FastAPI()



def load_data(file_path):
    with open(file_path, 'r') as f:
        return json.load(f)
    
def save_data(file_path, data):
    with open(file_path, 'w') as f:
        json.dump(data, f, indent=4)


@app.get("/")
async def root():
    return {"message": "this is my first fastapi project"}

@app.get('/about')
async def about():
    return {"message": "this is about page of my first fastapi project"}

@app.get("/view")
async def view():
    data = load_data("patients.json")
    return data

@app.get('/patinet/{patient_id}')
async def view_P(
    patient_id: str = Path(
        ...,
        description='the ID of patient to view',
        example='P001'
    )
):
    data = load_data("patients.json")

    if patient_id in data:
        return data[patient_id]
    else:
        raise HTTPException(
            status_code=404,
            detail=f"Patient with ID {patient_id} not found"
        )

@app.get('/sort')
async def sort(
    sort_by: str = Query(
        ...,
        description='sort by bmi ,height ,weight'
    ),
    order=Query(
        'asc',
        description='order of sorting asc or desc'
    )
):
    valid_fields = ['bmi', 'height', 'weight']

    if sort_by not in valid_fields:
        raise HTTPException(
            status_code=400,
            detail=f"Invalid sort field. Valid fields are: {', '.join(valid_fields)}"
        )

    if order not in ['asc', 'desc']:
        raise HTTPException(
            status_code=400,
            detail="Invalid order. Valid orders are: asc, desc"
        )

    data = load_data("patients.json")

    sort_df = True if order == 'desc' else False

    sorted_data = sorted(
        data.values(),
        key=lambda x: x.get(sort_by, 0),
        reverse=sort_df
    )

    return sorted_data

@app.post('/add')
async def add_patient(pat: patient):
    data=load_data("patients.json")

    if pat.id in data:
        raise HTTPException(
            status_code=400,
            detail=f"Patient with ID {pat.id} already exists"
        )
    
    data[pat.id] = pat.model_dump(exclude=['id'])

    save_data("patients.json", data)

    return JSONResponse(
        status_code=201,  
        content={"message": "Patient added successfully"}
    )

@app.put("/update/{patient_id}")
def update_patient(patient_id: str, pat: PatientUpdate):

    data = load_data("patients.json")

    if patient_id not in data:
        raise HTTPException(
            status_code=404,
            detail="Patient does not exist"
        )

    valid_pat = data[patient_id]

    updates = pat.model_dump(exclude_unset=True)

    for key, value in updates.items():
        valid_pat[key] = value

    valid_pat["id"] = patient_id

    updated_patient = patient(**valid_pat)

    data[patient_id] = updated_patient.model_dump(exclude={"id"})

    save_data("patients.json", data)

    return JSONResponse(
        status_code=200,
        content={
            "message": "Patient updated successfully",
            "patient": data[patient_id]
        }
    )

@app.delete('/delete/{patient_id}')
def delete(patient_id:str):
    data=load_data("patients.json")
    if patient_id not in data:
        raise HTTPException(status_code=404,detail="patiemy not exist")
    del data[patient_id]
    save_data('patients.json',data)
    return JSONResponse(
        status_code=200,content="delted"
    )
