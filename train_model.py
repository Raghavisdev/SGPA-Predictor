import pandas as pd
import joblib
from sklearn.ensemble import RandomForestRegressor
from sklearn.model_selection import train_test_split

# Load dataset
df = pd.read_csv("Student_Performance_2026.csv")

# Behavior-only features
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

# Train-test split (important for behavior-only model)
X_train, X_test, y_train, y_test = train_test_split(
    X, y, test_size=0.2, random_state=42
)

# Random Forest (non-linear, behavior-friendly)
model = RandomForestRegressor(
    n_estimators=400,
    max_depth=8,
    min_samples_leaf=15,
    random_state=42
)

model.fit(X_train, y_train)

# Save model and schema
joblib.dump(model, "behavior_only_model.pkl")
joblib.dump(behavior_features, "behavior_features.pkl")

print("✅ Behavior-only model trained and saved")