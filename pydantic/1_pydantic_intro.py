from pydantic import BaseModel, EmailStr, AnyUrl, Field
from typing import List, Dict, Optional, Annotated

class Patient(BaseModel):
    
    name: str = Annotated[str,
                          Field(max_length=180,
                                title="Name of the patient",
                                description="Give your full name",
                                examples=['Rudra', 'Z'])]
    
    age: int = Field(gt=0, lt=150)
    email: EmailStr
    linkedin_url = Optional[AnyUrl]
    weight: Annotated[float, Field(gt=0, strict=False)]
    
    married: Annotated[bool,
                       Field(default=None,
                             description="Is the patient married or not",
                             examples=['True', 'False'])]
    
    allergies: Annotated[Optional[List[str]],
                         Field(default=None,
                               max_length=10)]
                                  
    contact_details: Dict[str, str]
    

def insert_patient_data(patient: Patient):
    
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
insert_patient_data(patient)