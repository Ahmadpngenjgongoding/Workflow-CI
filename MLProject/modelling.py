"""
modelling.py (versi Workflow-CI)
Dijalankan otomatis oleh GitHub Actions lewat `mlflow run .` setiap ada trigger.
Melatih ulang (retrain) model menggunakan dataset hasil preprocessing yang sudah
disertakan di repo ini (dataset_preprocessing/diabetes_preprocessing.csv).
"""

import os
import pandas as pd
import mlflow
from sklearn.model_selection import train_test_split
from sklearn.ensemble import RandomForestClassifier
from sklearn.metrics import accuracy_score

BASE_DIR = os.path.dirname(os.path.abspath(__file__))
DATA_PATH = os.path.join(BASE_DIR, "dataset_preprocessing", "diabetes_preprocessing.csv")
RUN_ID_PATH = os.path.join(BASE_DIR, "run_id.txt")


def main():
    df = pd.read_csv(DATA_PATH)
    X = df.drop(columns=["Outcome"])
    y = df["Outcome"]
    X_train, X_test, y_train, y_test = train_test_split(
        X, y, test_size=0.2, random_state=42, stratify=y
    )

    mlflow.autolog()

    with mlflow.start_run(run_name="CI_Retrain_RandomForest") as run:
        model = RandomForestClassifier(n_estimators=100, max_depth=5, random_state=42)
        model.fit(X_train, y_train)

        y_pred = model.predict(X_test)
        acc = accuracy_score(y_test, y_pred)
        print(f"[CI] Retraining selesai. Akurasi: {acc:.4f}")

        # Simpan run_id supaya workflow CI bisa dipakai untuk build Docker image
        with open(RUN_ID_PATH, "w") as f:
            f.write(run.info.run_id)
        print(f"[CI] Run ID: {run.info.run_id}")


if __name__ == "__main__":
    main()
