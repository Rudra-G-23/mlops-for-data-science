import os
import pandas as pd
from sklearn.linear_model import LogisticRegression
import pickle

os.makedirs("dvc/model/", exist_ok=True)

df = pd.read_csv("dvc/data/processed/clean_data.csv")

X = df[["age", "salary"]]
y = df['purchased']

model = LogisticRegression()
model.fit(X, y)

with open("dvc/model/model.pkl", "wb") as f:
    pickle.dump(model, f)
    
print("Model training completed!")