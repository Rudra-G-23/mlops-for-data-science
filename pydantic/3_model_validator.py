""" 
If user age is greater than 60
then contact details must have the phone number.
"""
from pydantic import BaseModel, EmailStr, model_validator
from typing import List, Dict

class Patient(BaseModel):

    name: str
    age: int
    contact_details: Dict[str, str]

    @model_validator(mode='after')
    def validate_emergency_contact(cls, model):
        if model.age > 60 and 'emergency' not in model.contact_details:
            raise ValueError("Patients older than 60 must have an emergency contact")
        return model


def update_patient_data(patient: Patient):

    print(patient.name)
    print(patient.age)
    print(patient.contact_details)
    
    print('\n\nupdated')
      
patient_info = {
    'name': 'Rudra Prasad Bhuyan',
    'age': 60,
    'email': 'rudra@hdfc.com',
    'contact_details': {'emergency': '1234567890'}
}

patient = Patient(**patient_info)
update_patient_data(patient)