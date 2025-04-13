🫀 Heart Attack Risk Predictor

This project is a machine learning-powered web application that predicts the likelihood of a person having heart disease based on clinical data. The app is built using Streamlit and uses a trained classification model to provide predictions.


🌐 Try the live demo:

👉 heart-attack-risk-predictor.streamlit.app


📊 Features

Predicts heart disease risk based on user inputs

User-friendly interface with helpful explanations for each input

Educates users on how to obtain required medical test results

Built with scikit-learn, pandas, Streamlit, and joblib

Deployed to Streamlit Cloud for easy access


🧠 Model Inputs

The model uses the following inputs to make predictions:

Feature	Description

Age	Your age in years

Sex	Male or Female

Chest Pain Type	Type of chest pain experienced (e.g., typical angina, asymptomatic, etc.)

Resting Blood Pressure	Measured in mm Hg

Cholesterol	Serum cholesterol in mg/dl (requires a blood test)

Fasting Blood Sugar	> 120 mg/dl (requires a blood test)

Resting ECG Results	Results from resting electrocardiogram

Maximum Heart Rate Achieved	Typically measured during a stress test

Exercise Induced Angina	Chest pain during exercise

Oldpeak	ST depression induced by exercise relative to rest

Slope of ST Segment	Slope of the peak exercise ST segment

Number of Major Vessels	Detected by fluoroscopy (0–3)

Thalassemia	A blood disorder measured via blood tests or scans


🧪 How to Get the Medical Values

Some values require medical tests:

Cholesterol and Fasting Blood Sugar: Ask for a basic lipid panel and glucose test at a clinic or hospital.

Resting ECG & ST Depression: Performed during an electrocardiogram (ECG).

Maximum Heart Rate Achieved & ST Slope: These are measured during a stress test.

Thalassemia: Identified through a thalassemia screening or genetic test.

Please consult your doctor or medical professional for help acquiring this data.


🛠️ Running Locally

Prerequisites

Python 3.8+

Virtual environment (recommended)

Setup

# Clone the repository
    
    git clone https://github.com/Meliodus254/Heart-Attack-Risk-Predictor.git
    cd Heart-Attack-Risk-Predictor

# Create and activate virtual environment (optional)

    python -m venv env
    source env/bin/activate  # On Windows use: env\Scripts\activate

# Install dependencies

    pip install -r requirements.txt

# Run the app

    streamlit run app.py
    
📁 Project Structure

├── app.py                  # Streamlit app
├── model.pkl               # Trained ML model
├── requirements.txt        # Python dependencies
├── README.md               # Project documentation


🙏 Acknowledgements

UCI Heart Disease Dataset

Streamlit for the amazing UI framework

scikit-learn for ML tools

📬 Contact
For questions, feel free to reach out via GitHub or open an issue.
