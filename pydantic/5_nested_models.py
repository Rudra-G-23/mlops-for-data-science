from pydantic import BaseModel

class Address(BaseModel):

    city: str
    state: str
    pin: str

class Patient(BaseModel):

    name: str
    gender: str
    age: int
    address: Address

address_01 = {
    'city': 'Rourkela',
    'state': 'Odisha',
    'pin': '111111'
}

user_address =  Address(**address_01)

patient_01 = {
    'name': 'Rudra',
    'gender': 'Male',
    'age': 20,
    'address': user_address
}

patient = Patient(**patient_01)
print(patient)