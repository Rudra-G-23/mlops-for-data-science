import os
import pandas as pd
import mlflow

import matplotlib.pyplot as plt
import seaborn as sns

from sklearn.datasets import load_wine
from sklearn.model_selection import train_test_split
from sklearn.metrics import * 

from sklearn.ensemble import RandomForestClassifier

os.makedirs("images/mlflow", exist_ok=True)

# load datasets
wine = load_wine()
X = wine.data
y = wine.target

feature_names = wine.feature_names

X_train, X_test, y_train, y_test = train_test_split(
    X, y, test_size=0.2, random_state=42
)

# define para
MAX_DEPTH = 15
N_ESTIMATORS = 8

# Experiment tracking
with mlflow.start_run():
    
    # define model 
    rf = RandomForestClassifier(
        max_depth=MAX_DEPTH,
        n_estimators=N_ESTIMATORS,
        random_state=42
    )
    
    rf.fit(X_train, y_train)
    y_pred = rf.predict(X_test)
    
    accuracy = accuracy_score(y_test, y_pred)
    
    # Metrics
    mlflow.log_metric("accuracy", accuracy)
    
    # Para
    mlflow.log_param("max_depth", MAX_DEPTH)
    mlflow.log_param("n_estimators", N_ESTIMATORS)
    
    # Confusion matrix
    cm = confusion_matrix(y_test, y_pred)

    sns.heatmap(cm, annot=True, cmap="Blues", fmt="d")
    plt.title("Confusion Matrix")
    plt.xlabel("Predicted")
    plt.ylabel("Actual")
    plt.savefig("images/mlflow/confusion_matrix.png")
    mlflow.log_artifact("images/mlflow/confusion_matrix.png")
    plt.close()
    
    # Features imp
    importances = rf.feature_importances_
    df = pd.DataFrame({
        "feature": feature_names,
        "importance": importances
    }).sort_values("importance", ascending=False)
    
    plt.figure(figsize=(8, 4))
    sns.barplot(x="importance", y="feature", data=df)
    plt.title("Feature Importance")
    
    plt.savefig("images/mlflow/feature_importance.png")
    mlflow.log_artifact("images/mlflow/feature_importance.png")
    plt.close()
    
    # Code file
    mlflow.log_artifact(__file__)
    
    # Log model
    mlflow.sklearn.log_model(rf, "random_forest_model")
    
    # Tags
    mlflow.set_tags({
        "dataset": "wine",
        "model_type": "RadomForest",
    })