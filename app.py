import streamlit as st
from predictor import predict_sgpa

st.set_page_config(page_title="Behavior-Based SGPA Predictor")

st.title("🎓 Behavior-Based SGPA Predictor")
st.markdown(
    """
This model predicts SGPA **purely from behavioral factors**.
No past academic scores are used.

Use this as a **habit analysis & improvement tool**, not a final grade oracle.
"""
)

st.header("📥 Enter Daily Behavior")

online = st.slider("Online Study Hours", 0.0, 6.0, 3.0, 0.5)
offline = st.slider("Offline Study Hours", 0.0, 5.0, 2.0, 0.5)
attendance = st.slider("Attendance (%)", 50, 100, 75)
sleep = st.slider("Sleep Hours", 5.0, 9.0, 7.0, 0.5)
gaming = st.slider("Gaming Hours", 0.0, 4.0, 1.5, 0.5)
social = st.slider("Social Media Hours", 0.0, 4.0, 2.5, 0.5)
screen = st.slider("Total Screen Time", 4.0, 10.0, 7.0, 0.5)

if st.button("🔮 Predict SGPA"):
    student = {
        "online_study_hours": online,
        "offline_study_hours": offline,
        "attendance_percentage": attendance,
        "sleep_hours": sleep,
        "gaming_hours": gaming,
        "social_media_hours": social,
        "daily_screen_time_hours": screen
    }

    sgpa = predict_sgpa(student)

    st.success(f"📊 Predicted SGPA: **{sgpa}**")

    st.info(
        "ℹ️ This prediction reflects behavioral patterns. "
        "Accuracy will improve as more diverse behavioral data is added."
    )