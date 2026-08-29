import os
import pickle
import streamlit as st

# Build the path to the model file relative to this script
BASE_DIR = os.path.dirname(__file__)
model_path = os.path.join(BASE_DIR, "log_reg_model.pkl")

# Load the model safely
with open(model_path, "rb") as f:
    model = pickle.load(f)

# Streamlit app UI
st.title("Diabetes Prediction App")

# Input fields
pregnancies = st.number_input("Number of Pregnancies", min_value=0, max_value=20, value=0)
glucose = st.number_input("Glucose Level", min_value=0, max_value=300, value=120)
blood_pressure = st.number_input("Blood Pressure", min_value=0, max_value=200, value=70)
skin_thickness = st.number_input("Skin Thickness", min_value=0, max_value=100, value=20)
insulin = st.number_input("Insulin Level", min_value=0, max_value=900, value=80)
bmi = st.number_input("BMI", min_value=0.0, max_value=70.0, value=25.0)
dpf = st.number_input("Diabetes Pedigree Function", min_value=0.0, max_value=3.0, value=0.5)
age = st.number_input("Age", min_value=1, max_value=120, value=30)

# Prediction button
if st.button("Predict"):
    input_data = [[pregnancies, glucose, blood_pressure, skin_thickness,
                   insulin, bmi, dpf, age]]
    prediction = model.predict(input_data)
    if prediction[0] == 1:
        st.error("⚠️ The model predicts: Diabetes Positive")
    else:
        st.success("✅ The model predicts: Diabetes Negative")
