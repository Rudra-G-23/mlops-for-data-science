""" 
GOAL: Auto log with mlflow
"""
import os
import mlflow

import matplotlib.pyplot as plt
import seaborn as sns

from sklearn.datasets import load_wine
from sklearn.model_selection import train_test_split
from sklearn.metrics import accuracy_score, confusion_matrix
from sklearn.ensemble import RandomForestClassifier

os.environ["PYSPARK_PIN_THREAD"] = "false"

mlflow.set_tracking_uri("sqlite:///mlflow.db")
mlflow.set_experiment("Wine RF Experiment")

mlflow.autolog()

os.makedirs("images/mlflow", exist_ok=True)

wine = load_wine()
X = wine.data
y = wine.target

X_train, X_test, y_train, y_test = train_test_split(
    X, y, test_size=0.2, random_state=42
)

MAX_DEPTH = 15
N_ESTIMATORS = 8

with mlflow.start_run(run_name="rf_wine_run_1"):

    rf = RandomForestClassifier(
        max_depth=MAX_DEPTH,
        n_estimators=N_ESTIMATORS,
        random_state=42
    )

    rf.fit(X_train, y_train)

    y_pred = rf.predict(X_test)

    accuracy = accuracy_score(y_test, y_pred)

    cm = confusion_matrix(y_test, y_pred)

    sns.heatmap(cm, annot=True, cmap="Blues", fmt="d")
    plt.title("Confusion Matrix")

    plt.savefig("images/mlflow/cm.png")
    plt.close()

    mlflow.log_artifact("images/mlflow/cm.png")