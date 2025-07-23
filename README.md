# Aircraft-Maintenance-Prediction
Developed ML-based predictive model for aircraft engine failure prediction with high accuracy for preventive maintenance decisions.
# ✈️ Aircraft Engine Failure Prediction – Flask Web App

This project is a Flask-based web application that predicts the likelihood of an aircraft engine failure based on various input parameters. It leverages a trained **Random Forest classifier** and **MinMaxScaler** to perform accurate predictions.

---

## 🚀 Features

- ✅ Clean and modern aircraft dashboard-style UI
- 🧠 Uses trained `RandomForest.pkl` model for prediction
- 🔧 Preprocessing with `Scaler.pkl` (MinMax or Standard Scaler)
- 📊 Real-time prediction based on user input
- 🌐 Built with Flask and Bootstrap 5 for responsive design

---

## 🗂️ Project Structure

AircraftEnginePredictor/
├── app.py # Flask application logic
├── RandomForest.pkl # Trained ML model
├── Scaler.pkl # Pre-fitted scaler for input normalization
├── templates/
│ └── modern_aircraft_ui.html # UI template
├── static/
│ └── (optional CSS/JS/images)
├── requirements.txt # Python dependencies
└── README.md # Project documentation
