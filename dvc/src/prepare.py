import os
import pandas as pd

os.makedirs("dvc/data/processed/", exist_ok=True)

df = pd.read_csv("dvc/data/raw/data.csv")

df['salary'] = df['salary'] / 1000

df.to_csv("dvc/data/processed/clean_data.csv", index=False)

print("Data Preprocessing done!")