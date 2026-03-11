import os
import json
from fastapi import FastAPI, Path, HTTPException, Query

app = FastAPI()
patient_file_path = os.path.join("api/data", "patients.json")

def _load_data():
    """Load from the db."""
    with open(patient_file_path, 'r') as f:
        data = json.load(f)
        return data
        
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