import os
import json
from fastapi import FastAPI

app = FastAPI()
patient_file_path = os.path.join("api/data", "patients.json")

def _load_data():
    with open(patient_file_path, 'r') as f:
        data = json.load(f)
        return data
        
@app.get("/")
def hello():
    return {
        "message": "Patient Management System"
    }

@app.get("/about")
def about():
    return {
        "message": "A functional API."
    }

@app.get("/view")
def view_data():
    data = _load_data()
    return data