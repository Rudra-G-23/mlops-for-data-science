
""" 
Give your email to get the benefits.
Who are employee of bank company.
"""
from pydantic import BaseModel, EmailStr, Field, field_validator
from typing import List, Dict, Optional, Annotated

class Patient(BaseModel):
    
    name: str
    age: int
    email: EmailStr

    
    @field_validator('email')
    @classmethod
    def email_validator(cls, value):
        
        valid_domains = ['hdfc.com', 'icici.com']
        domain_name = value.split('@')[-1]
        
        if domain_name not in valid_domains:
            raise ValueError('You are not an employee of the bank or Wrong email')
        
        return value
    
    @field_validator('name', mode='after')
    @classmethod
    def transform_name(cls, value):
        return value.upper()
    
    @field_validator('age', mode='before')
    @classmethod
    def check_age(cls, value):
        """If user give the str then it give error.
        but if we give the 'after' then it give proper format.
        
        after -> after user input
        before -> User input before input
        """
        if 0 < value < 100:
            return value
        raise ValueError('Age should be between 0 and 100')

def update_patient_data(patient: Patient):
    
    print(f"Hello! {patient.name}")
    print(f"Your email: {patient.email}")

    print("\n\nSuccess")

patient_info_2 = {
    'name': 'Rudra Prasad Bhuyan',
    'age': 20,
    'email': 'rudra@hdfc.com',
}

patient = Patient(**patient_info_2)
update_patient_data(patient)