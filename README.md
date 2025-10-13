## ⚙️ Electric Motor Temperature Prediction using Machine Learning

### 🧾 Overview

This project predicts the **Permanent Magnet (PM) temperature** of an electric motor based on parameters like ambient temperature, coolant temperature, motor speed, voltage, and current.
It helps in **preventive maintenance**, avoiding overheating, and improving the reliability of industrial motors.

---

### 🚀 Features

* Machine Learning–based temperature prediction
* Flask web interface for manual input
* Simple and user-friendly HTML frontend
* Model trained and evaluated on real motor data
* Scalable and ready for cloud deployment

---

### 🧠 Algorithms Used

We trained and compared the following regression algorithms:

* Linear Regression
* Decision Tree Regressor
* Random Forest Regressor
* Support Vector Regressor (SVR)

After comparison, the **Decision Tree Regressor** showed the best performance and was selected as the final model.

---

### 📂 Project Structure

```
Electric_Motor_Temperature_Prediction/
│
├── app.py
├── requirements.txt
├── templates/
│   ├── manual_predict.html
│   └── glossary.html
│
├── static/
│   ├── styles.css
│   └── motor1.gif
│
├── model.save
├── transform.save
├── measures_v2.csv
└── README.md
```

---

### 💡 How to Run

1. Install dependencies

   ```
   pip install -r requirements.txt
   ```

2. Run the Flask app

   ```
   python app.py
   ```

3. Open your browser and go to
   👉 [http://127.0.0.1:5000](http://127.0.0.1:5000)

4. Enter motor parameters and click **Predict** to see the temperature output.

---

### 📊 Dataset & Model

The dataset and trained model are large files, so they are hosted externally.
You can download them here:

* 📘 **Dataset:** [Download measures_v2.csv](https://www.kaggle.com/datasets/wkirgsn/electric-motor-temperature)
* 🤖 **Trained Model:** [Download model.save](https://drive.google.com/file/d/1G-9-eyCl5of6NezKX763n4ODcQcDXM8U/view?usp=sharing)

---

### 📸 Demo

* GitHub Repository: [https://github.com/muralikrishna4526/Electric-Motor-Temperature-Prediction](#)
* Demo Video: [https://drive.google.com/your_demo_video_link](#)

---

### 🧰 Technologies Used

* Python
* Flask
* Scikit-learn
* HTML / CSS
* Matplotlib & Seaborn

---

