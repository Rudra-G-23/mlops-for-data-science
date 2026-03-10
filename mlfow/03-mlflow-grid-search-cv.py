import os
import mlflow
from sklearn.datasets import load_wine
from sklearn.model_selection import train_test_split, GridSearchCV
from sklearn.ensemble import RandomForestClassifier
from sklearn.metrics import accuracy_score

os.environ["PYSPARK_PIN_THREAD"] = "false"
mlflow.set_tracking_uri("sqlite:///mlflow.db")
mlflow.set_experiment("Wine GridSearch Experiment")

# dataset
wine = load_wine()
X = wine.data
y = wine.target

X_train, X_test, y_train, y_test = train_test_split(
    X, y, test_size=0.2, random_state=42
)

# hyperparameter grid
param_grid = {
    "max_depth": [5, 10, 15],
    "n_estimators": [50, 100]
}

# base model
rf = RandomForestClassifier(random_state=42)

# grid search
grid = GridSearchCV(
    estimator=rf,
    param_grid=param_grid,
    cv=3,
    scoring="accuracy"
)

# Parent Run
with mlflow.start_run(run_name="GridSearch_RF_Parent") as parent_run:

    grid.fit(X_train, y_train)

    # best model
    best_model = grid.best_estimator_

    y_pred = best_model.predict(X_test)

    acc = accuracy_score(y_test, y_pred)

    # log best results in parent
    mlflow.log_metric("best_test_accuracy", acc)
    mlflow.log_params(grid.best_params_)

    # Child Runs
    results = grid.cv_results_

    for i in range(len(results["params"])):

        with mlflow.start_run(
            run_name=f"child_run_{i}",
            nested=True
        ):

            params = results["params"][i]

            mlflow.log_params(params)

            mlflow.log_metric(
                "mean_cv_score",
                results["mean_test_score"][i]
            )