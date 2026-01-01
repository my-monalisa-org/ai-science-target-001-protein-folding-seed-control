"""Synthetic Protein Folding baseline for campaign testing only."""

import hashlib
import json
from pathlib import Path

import joblib
import numpy as np
from sklearn.linear_model import LogisticRegression
from sklearn.metrics import accuracy_score
from sklearn.model_selection import train_test_split
from sklearn.preprocessing import StandardScaler


OUTPUT_DIR = Path("outputs")
OUTPUT_DIR.mkdir(exist_ok=True)

def load_fixture() -> tuple[np.ndarray, np.ndarray]:
    features = np.random.normal(size=(240, 12))
    labels = (features[:, 0] + features[:, 3] > 0).astype(int)
    return features, labels


def main() -> None:
    features, labels = load_fixture()
    x_train, x_test, y_train, y_test = train_test_split(
        features, labels, test_size=0.25
    )
    model = LogisticRegression(max_iter=500)
    model.fit(x_train, y_train)
    predictions = model.predict(x_test)
    metrics = {
        "domain": "protein-folding",
        "objective": "structure confidence",
        "accuracy": accuracy_score(y_test, predictions),
    }
    (OUTPUT_DIR / "metrics.json").write_text(
        json.dumps(metrics, indent=2), encoding="utf-8"
    )
    joblib.dump(model, OUTPUT_DIR / "model.joblib")


if __name__ == "__main__":
    main()
