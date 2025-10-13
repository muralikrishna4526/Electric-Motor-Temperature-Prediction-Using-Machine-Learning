from flask import Flask, render_template, request
import joblib
import numpy as np

# Load saved model and scaler
model = joblib.load("D:/VMK/flask_app/model.save")
scaler = joblib.load("D:/VMK/flask_app/transform.save")

app = Flask(__name__)

# Home page (GET only)
@app.route("/", methods=["GET"])
def home():
    return render_template("home.html")

# Glossary route
@app.route('/glossary')
def glossary():
    return render_template('glossary.html')

# Manual prediction page (GET and POST)
@app.route("/manual_predict", methods=["GET", "POST"])
def manual_predict():
    prediction = None
    temp_state = None  # Initialize here
    if request.method == "POST":
        try:
            # Collect values from form
            ambient = float(request.form['ambient'])
            coolant = float(request.form['coolant'])
            u_d = float(request.form['u_d'])
            u_q = float(request.form['u_q'])
            motor_speed = float(request.form['motor_speed'])
            i_d = float(request.form['i_d'])
            i_q = float(request.form['i_q'])

            # Prepare input for model
            input_data = np.array([[ambient, coolant, u_d, u_q, motor_speed, i_d, i_q]])
            input_scaled = scaler.transform(input_data)
            prediction = model.predict(input_scaled)[0]
            prediction = round(prediction, 2)

               # Determine temperature state
            if prediction < 50:
                temp_state = "Cooled"
            elif 50 <= prediction <= 80:
                temp_state = "Normal"
            else:
                temp_state = "Overheated"

        except Exception as e:
            prediction = f"Error: {e}"

    return render_template("manual_predict.html", prediction=prediction,temp_state=temp_state)

if __name__ == "__main__":
    app.run(debug=True)