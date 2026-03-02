import pandas as pd
import joblib
import numpy as np

# Load model artifacts
model = joblib.load("behavior_only_model.pkl")
behavior_features = joblib.load("behavior_features.pkl")

def predict_sgpa(input_data: dict):
    """
    Predict SGPA using ONLY behavioral features
    """

    X = pd.DataFrame([{f: input_data[f] for f in behavior_features}])

    sgpa = float(model.predict(X)[0])

    # Safety bounds
    sgpa = float(np.clip(sgpa, 5.0, 10.0))

    return round(sgpa, 2)