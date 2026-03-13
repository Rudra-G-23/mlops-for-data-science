import os
import json
from pydantic import BaseModel, Field, computed_field
from fastapi.responses import JSONResponse
from typing import Annotated, Literal
from fastapi import FastAPI, Path, HTTPException, Query

app = FastAPI()
patient_file_path = os.path.join("api/data", "patients.json")

class Patient(BaseModel):
    
    id: Annotated[str,
                  Field(...,
                        description="ID of the patient",
                        examples=["P001", "P030"])]
    name: Annotated[str,
                    Field(...,
                          description="Name of the Patient")]
    city: Annotated[str,
                    Field(...,
                          description="Patient City")]
    age: Annotated[int,
                   Field(...,
                         gt=0,
                         lt=150,
                         description="Age of the patient")]
    gender: Annotated[Literal['Male', 'Female', 'Other'],
                      Field(..., description="Gender of the patient")]
    height: Annotated[float,
                      Field(..., 
                            gt=0,
                            description="Height of the patient in meters")] 
    weight: Annotated[float,
                      Field(...,
                            gt=0,
                            description="Weight of the patient in kgs")]

    @computed_field
    @property
    def bmi(self) -> float:
        return round(self.weight / (self.height ** 2), 2)
    
    @computed_field
    @property
    def verdict(self) -> str:
        
        if self.bmi < 18.5:
            return "Under Weight"
        elif self.bmi < 30:
            return "Normal"
        else:
            return "Over Weight"

def _load_data():
    """Load from the db."""
    with open(patient_file_path, 'r') as f:
        data = json.load(f)
        return data

def _save_data(data):
    """Save the data into db."""
    with open(patient_file_path, 'w') as f:
        return json.dump(data, f)
    
@app.get("/")
def hello():
    """Intro of the api"""
    return {
        "message": "Patient Management System"
    }

@app.get("/about")
def about():
    """What this api do"""
    return {
        "message": "A functional API."
    }

@app.get("/view")
def view_data():
    """Load all the data form db"""
    data = _load_data()
    return data

# Path params
@app.get("/patient/{patient_id}")
def view_patient(patient_id: str = Path(..., 
                                        description="ID of the patient in DB.",
                                        example="P001"
                                        )):
    
    data = _load_data()

    if patient_id in data:
        return data[patient_id]

    raise HTTPException(status_code=404, detail="Patient id not found in DB.")

# Query para (/sort?sort_by=height&order=asc)
@app.get("/sort")
def sort_patient(sort_by:str = Query(...,description="Sort on the basic of height, weight, bmi"),
                 order: str = Query('asc', description="Sort in asc or desc order")):
    
    valid_fields = ['height', 'weight', 'bmi']
    
    if sort_by not in valid_fields:
        raise HTTPException(status_code=404, detail=f"Invalid field select {valid_fields}")
    if order not in ['asc', 'desc']:
        raise HTTPException(status_code=404, detail="Invalid oder select between asc, desc")

    data = _load_data()
    
    sort_order = True if order == 'desc' else False
    
    sorted_data = sorted(data.values(), key=lambda x: x.get(sort_by, 0), reverse= sort_order)
    
    return sorted_data

@app.post("/create")
def create_patient(patient: Patient):
    
    # load the existing data
    data = _load_data()
    
    # check if hte patient already exist
    if patient.id in data:
        raise HTTPException(status_code=404,detail="Patient already exists.")
    
    # new patient add to db
    data[patient.id] = patient.model_dump(exclude=['id'])
    
    # save into json file
    _save_data(data)
    
    return JSONResponse(status_code=201, content={'message': 'Patient created successfully.'})