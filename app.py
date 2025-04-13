import streamlit as st
import pandas as pd
import joblib

# Load the trained model
model = joblib.load("model.pkl")

# Streamlit setup
st.set_page_config(page_title="Heart Disease Risk Prediction", layout="centered")
st.title("💓 Heart Disease Risk Prediction App")

# Description
st.markdown("""
Welcome to the **Heart Disease Risk Prediction App**.

This tool uses machine learning to estimate your risk of heart disease based on information you provide.
Please answer the questions below as accurately as possible. If you're unsure about any medical values, consult a healthcare provider or get a medical test.
""")

st.info("⚠️ This is a health guidance tool and does **not** replace professional medical advice.")

# --- INPUTS ---

# Age
age = st.number_input("1. Age (in years)", min_value=1, max_value=120, value=30,
                      help="Enter your current age.")

# Sex
sex = st.selectbox("2. Sex", ["Male", "Female"], help="Select your biological sex.")
sex = 1 if sex == "Male" else 0

# Chest Pain Type
cp = st.selectbox(
    "3. Chest Pain Type",
    ["Typical Angina", "Atypical Angina", "Non-anginal Pain", "Asymptomatic"],
    help="""Choose the description that best fits your chest pain:
- Typical Angina: Predictable chest pain with exertion.
- Atypical Angina: Unusual chest pain, may not relate to exertion.
- Non-anginal: Chest discomfort not related to heart problems.
- Asymptomatic: No chest pain.
"""
)
cp_map = {
    "Typical Angina": 0,
    "Atypical Angina": 1,
    "Non-anginal Pain": 2,
    "Asymptomatic": 3
}
cp = cp_map[cp]

# Resting Blood Pressure
trtbps = st.number_input("4. Resting Blood Pressure (mm Hg)", min_value=80, max_value=200, value=120,
                         help="Measure this using a home blood pressure monitor or ask your doctor.")

# Cholesterol
chol = st.number_input("5. Cholesterol Level (mg/dL)", min_value=100, max_value=400, value=200,
                       help="🧪 You can obtain this value through a lipid profile blood test at a clinic.")

# Fasting Blood Sugar
fbs = st.selectbox("6. Is your fasting blood sugar > 120 mg/dL?", ["Yes", "No"],
                   help="🧪 Requires a fasting blood sugar test (usually done after 8–12 hours of fasting).")
fbs = 1 if fbs == "Yes" else 0

# Resting ECG
restecg = st.selectbox(
    "7. Resting Electrocardiographic Result",
    ["Normal", "ST-T Wave Abnormality", "Left Ventricular Hypertrophy"],
    help="""Ask a doctor for a resting ECG (Electrocardiogram) test. Results include:
- Normal: No abnormalities.
- ST-T Wave Abnormality: Signs of ischemia or past heart attack.
- Left Ventricular Hypertrophy: Thickening of heart's left chamber.
"""
)
restecg_map = {
    "Normal": 0,
    "ST-T Wave Abnormality": 1,
    "Left Ventricular Hypertrophy": 2
}
restecg = restecg_map[restecg]

# Max heart rate
thalachh = st.number_input("8. Maximum Heart Rate Achieved (bpm)", min_value=60, max_value=220, value=150,
                           help="Usually measured during a treadmill (stress) test.")

# Exercise Induced Angina
exng = st.selectbox("9. Do you feel chest pain during exercise?", ["Yes", "No"],
                    help="This indicates angina triggered by physical activity.")
exng = 1 if exng == "Yes" else 0

# Oldpeak
oldpeak = st.number_input("10. ST Depression Induced by Exercise", min_value=0.0, max_value=6.0, value=1.0,
                          help="🧪 Derived from a stress ECG test. Ask your doctor for this value.")

# Slope of ST Segment
slp = st.selectbox("11. Slope of the Peak Exercise ST Segment", ["Upsloping", "Flat", "Downsloping"],
                   help="""Ask a doctor for this detail after a stress ECG:
- Upsloping: Generally considered normal.
- Flat: Could be a sign of heart disease.
- Downsloping: Stronger indicator of risk.
""")
slp_map = {"Upsloping": 0, "Flat": 1, "Downsloping": 2}
slp = slp_map[slp]

# Major Vessels Colored by Fluoroscopy
caa = st.selectbox("12. Number of Major Vessels Colored by Fluoroscopy (0-3)", [0, 1, 2, 3],
                   help="🧪 Requires a coronary angiogram (X-ray test) to count vessels with blood flow.")

# Thalassemia
thall = st.selectbox("13. Thalassemia Type", ["Normal", "Fixed Defect", "Reversible Defect"],
                     help="""🧬 This is a type of blood disorder. Ask your doctor or check a thalassemia blood test report:
- Normal: No thalassemia.
- Fixed Defect: Permanent damage in blood flow.
- Reversible Defect: Temporary defect that can improve.
""")
thall_map = {
    "Normal": 1,
    "Fixed Defect": 2,
    "Reversible Defect": 3
}
thall = thall_map[thall]

# Prepare DataFrame
input_data = pd.DataFrame({
    "age": [age],
    "sex": [sex],
    "cp": [cp],
    "trtbps": [trtbps],
    "chol": [chol],
    "fbs": [fbs],
    "restecg": [restecg],
    "thalachh": [thalachh],
    "exng": [exng],
    "oldpeak": [oldpeak],
    "slp": [slp],
    "caa": [caa],
    "thall": [thall]
})

# Prediction
prediction = model.predict(input_data)

# Results
st.subheader("🧾 Prediction Result")
if prediction[0] == 1:
    st.error("**The model predicts: HIGH RISK of heart disease**")
    st.markdown("""
    💡 **Next steps:**
    - Consult a cardiologist immediately.
    - Request further testing such as ECG, stress test, or echocardiogram.
    - Consider lifestyle changes: diet, exercise, smoking cessation, stress reduction.
    """)
else:
    st.success("**The model predicts: LOW RISK of heart disease**")
    st.markdown("""
    ✅ You currently show low risk of heart disease.
    
    💡 Maintain a heart-healthy lifestyle:
    - Eat a balanced diet.
    - Exercise regularly.
    - Avoid smoking and excessive alcohol.
    - Monitor blood pressure and cholesterol annually.
    """)

st.caption("🔒 Your data is not stored or shared.")
