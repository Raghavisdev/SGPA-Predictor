from predictor import predict_sgpa

student = {
    "online_study_hours": 4.0,
    "offline_study_hours": 3.0,
    "attendance_percentage": 90,
    "sleep_hours": 8.0,
    "gaming_hours": 0.5,
    "social_media_hours": 1.5,
    "daily_screen_time_hours": 5.0
}

print("🎯 Predicted SGPA:", predict_sgpa(student))