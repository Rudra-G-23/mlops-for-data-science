# Sol 1: Type hinting
def insert_patient_data(name:str, age:int):
    
    print(f"Hello! {name}")
    print(f"Your age is {age}")
    print("Inserted into the database")

# Sol2 : Data type checking
def insert_patient_data(name:str, age:int):
    
    if type(name) == str and type(age) == int:
        print(f"Hello! {name}")
        print(f"Your age is {age}")
        print("Inserted into the database")
    else:
        raise TypeError("Incorrect data type")

# Sol 3 : Validate
def insert_patient_data(name:str, age:int):
    
    if type(name) == str and type(age) == int:
        if age < 0:
            raise ValueError("Age can't be negative.")
        else:
            print(f"Hello! {name}")
            print(f"Your age is {age}")
            print("Inserted into the database")
    else:
        raise TypeError("Incorrect data type")

# Problem
# 1. Force to give specific input format
# 2. How to handle the more variables
# 3. How to handle the specific requirement of any variables


insert_patient_data("Rudra", 20)