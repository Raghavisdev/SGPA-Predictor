## 🌐 Live Demo

👉 https://sgpa-predictor-r3nly.streamlit.app/



# 🎓 Behavior-Based SGPA Predictor

A machine learning project that predicts a student’s **Semester Grade Point Average (SGPA)** purely from **behavioral factors** such as study habits, sleep, attendance, and screen usage — **without relying on past academic scores**.

> ⚠️ This project is designed for **behavioral analysis and academic intervention**, not as a guaranteed grade prediction system.

---

## 🌐 Live Demo

👉 https://sgpa-predictor-r3nly.streamlit.app/

---

## 📌 Why This Project?

Most academic prediction systems rely heavily on **past grades**, which introduces bias and limits behavioral insight.

This project intentionally removes academic history and answers a different question:

> *“Given a student’s current habits and lifestyle, what academic performance range do these behaviors suggest?”*

The result is a **behavior-first, ethical, and explainable ML system**.

---

## 🚀 Features

- ✅ **Behavior-only model** (no previous SGPA leakage)
- 🌳 **Random Forest Regressor** to capture non-linear behavior effects
- 🎛 **Interactive Streamlit dashboard**
- 📊 Realistic, bounded SGPA predictions
- ☁️ **Deployed on Streamlit Cloud**
- 🔄 Auto-trains model on first deployment (cloud-safe)

---

## 🧠 Model Design


### Behavioral Features Used
- Online study hours
- Offline study hours
- Attendance percentage
- Sleep hours
- Gaming hours
- Social media usage
- Total daily screen time

No academic history (previous SGPA) is used.

---

## 🛠 Tech Stack

- **Python**
- **Pandas, NumPy**
- **Scikit-learn**
- **Random Forest Regressor**
- **Streamlit**
- **Joblib**
- **GitHub + Streamlit Cloud**

---

## 📂 Project Structure

SGPA-Predictor/
│
├── app.py # Streamlit UI
├── predictor.py # Model loading & prediction logic
├── train_model.py # Training script (local use)
├── test_run.py # CLI test script
├── Student_Performance_2026.csv
├── requirements.txt
├── README.md
└── .gitignore


> Note: Model files (`.pkl`) are intentionally not committed.  
> The app auto-trains the model on first cloud deployment.

---

## ▶️ Run Locally

### 1. Clone the repository
```bash

git clone https://github.com/Raghavisdev/SGPA-Predictor.git
cd SGPA-Predictor

pip install -r requirements.txt

streamlit run app.py

```
---

### ✅ What this README achieves
- Explains **why** the model exists
- Sets **correct expectations**
- Looks professional to recruiters
- Defends your design choices
- Matches the deployed behavior exactly

If you want next, I can:
- Write a **LinkedIn post** announcing this
- Improve UI wording for public users
- Add a **confidence badge** to the app
- Plan **v2 of the project**

Just tell me 👍


