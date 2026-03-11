""" 
Where user can't give.
We can fetch or create from existing data points.
Then we used the computed field.
"""

from pydantic import BaseModel, computed_field
from typing import List, Dict

class Patient(BaseModel):

    name: str
    age: int
    weight: float # Kg
    height: float # M
    
    @computed_field
    @property
    def bmi(self) -> float:
        bmi = round(self.weight/(self.height**2),2)
        return bmi


def update_patient_data(patient: Patient):

    print(patient.name)
    print(patient.age)
    print(patient.weight)    
    print(patient.height)
    
    print(f"{patient.bmi}")
    
    print('\n\nupdated')
      
patient_info = {
    'name': 'Rudra Prasad Bhuyan',
    'age': 60,
    'weight': 50,
    'height': 1.70
}

patient = Patient(**patient_info)
update_patient_data(patient)