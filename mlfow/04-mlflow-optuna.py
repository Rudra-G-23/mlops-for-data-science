import os
import optuna
import mlflow

from sklearn.datasets import load_wine
from sklearn.model_selection import train_test_split
from sklearn.ensemble import RandomForestClassifier
from sklearn.metrics import accuracy_score


# set experiment
os.environ["PYSPARK_PIN_THREAD"] = "false"
mlflow.set_tracking_uri("sqlite:///mlflow.db")
mlflow.set_experiment("Optuna_RF_Wine")

# dataset
wine = load_wine()
X = wine.data
y = wine.target

X_train, X_test, y_train, y_test = train_test_split(
    X, y, test_size=0.2, random_state=42
)


# Objective Function
def objective(trial):

    # hyperparameter search space
    max_depth = trial.suggest_int("max_depth", 3, 20)
    n_estimators = trial.suggest_int("n_estimators", 50, 200)

    # child run
    with mlflow.start_run(nested=True):

        model = RandomForestClassifier(
            max_depth=max_depth,
            n_estimators=n_estimators,
            random_state=42
        )

        model.fit(X_train, y_train)

        preds = model.predict(X_test)

        acc = accuracy_score(y_test, preds)

        # log params
        mlflow.log_param("max_depth", max_depth)
        mlflow.log_param("n_estimators", n_estimators)

        # log metric
        mlflow.log_metric("accuracy", acc)

    return acc


# Parent Run
with mlflow.start_run(run_name="Optuna_Optimization"):

    study = optuna.create_study(direction="maximize")

    study.optimize(objective, n_trials=10)

    # best params
    mlflow.log_params(study.best_params)

    mlflow.log_metric("best_accuracy", study.best_value)