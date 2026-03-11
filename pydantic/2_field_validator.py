
""" 
Give your email to get the benefits.
Who are employee of bank company.
"""
from pydantic import BaseModel, EmailStr, AnyUrl, Field
from typing import List, Dict, Optional, Annotated

class Patient(BaseModel):
    
    name: str 
    age: int 
    email: EmailStr
    weight: float
    married: bool
    allergies: List[str]
    contact_details: Dict[str, str]
    

def update_patient_data(patient: Patient):
    
    print(f"Hello! {patient.name}")
    print(f"Your age is {patient.age}")
    print(f"Your email please {patient.email}")
    print(f"Your Linkedin URL {patient.linkedin_url}")
    print(patient.allergies)
    
    print("Inserted into the database")

patient_info_2 = {
    'name': 'Rudra Prasad Bhuyan',
    'age': 20,
    'email': 'rudra@gmail.com',
    'weight': 50,
    'married': False,
    'allergies': ['Cool'],
    'contact_details': {'email': 'rudra@gmail.com'}
}

patient = Patient(**patient_info_2)
update_patient_data(patient)