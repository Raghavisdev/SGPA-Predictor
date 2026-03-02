import pandas as pd
import numpy as np
import joblib
import os
from sklearn.ensemble import RandomForestRegressor
import streamlit as st

MODEL_PATH = "behavior_only_model.pkl"
FEATURE_PATH = "behavior_features.pkl"
DATA_PATH = "Student_Performance_2026.csv"

@st.cache_resource
def load_or_train_model():
    # If model exists, load it
    if os.path.exists(MODEL_PATH) and os.path.exists(FEATURE_PATH):
        model = joblib.load(MODEL_PATH)
        features = joblib.load(FEATURE_PATH)
        return model, features

    # Otherwise train
    df = pd.read_csv(DATA_PATH)

    behavior_features = [
        "online_study_hours",
        "offline_study_hours",
        "attendance_percentage",
        "sleep_hours",
        "gaming_hours",
        "social_media_hours",
        "daily_screen_time_hours"
    ]

    X = df[behavior_features]
    y = df["current_sem_CGPA"]

    model = RandomForestRegressor(
        n_estimators=400,
        max_depth=8,
        min_samples_leaf=15,
        random_state=42
    )

    model.fit(X, y)

    joblib.dump(model, MODEL_PATH)
    joblib.dump(behavior_features, FEATURE_PATH)

    return model, behavior_features


# Load model once
model, behavior_features = load_or_train_model()


def predict_sgpa(input_data: dict):
    X = pd.DataFrame([{f: input_data[f] for f in behavior_features}])
    sgpa = float(model.predict(X)[0])
    return round(float(np.clip(sgpa, 5.0, 10.0)), 2)