from flask import Flask, render_template, request
import numpy as np
import joblib

app = Flask(__name__)

# Load model and scaler
model = joblib.load("RandomForest.pkl")
scaler = joblib.load("Scaler.pkl")

@app.route("/", methods=["GET", "POST"])
def home():
    prediction_text = ""
    
    if request.method == "POST":
        try:
            # Get values from the form
            features = [
                float(request.form.get("temperature")),
                float(request.form.get("pressure")),
                float(request.form.get("rotational_speed")),
                float(request.form.get("engine_health")),
                float(request.form.get("fuel_consumption")),
                float(request.form.get("vibration_level")),
                float(request.form.get("oil_temperature")),
                float(request.form.get("altitude")),
                float(request.form.get("humidity"))
            ]
            
            input_data = np.array([features])
            scaled_input = scaler.transform(input_data)
            prediction = model.predict(scaled_input)[0]

            prediction_text = (
                "⚠️ Engine Failure Detected – Maintenance Needed"
                if prediction == 1
                else "✅ Engine is Healthy – No Maintenance Required"
            )
        except:
            prediction_text = "❌ Invalid input! Please enter numeric values only."

    return render_template("index.html", prediction=prediction_text)

if __name__ == "__main__":
    app.run(debug=True)
