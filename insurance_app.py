# insurance_app.py

import streamlit as st
import pandas as pd
import numpy as np
import joblib  # to load saved model
from sklearn.ensemble import GradientBoostingRegressor

# Load the model
@st.cache_resource
def load_model():
    model = joblib.load('gradient_boost_model.pkl')
    return model

model = load_model()

# Streamlit UI
st.title("💸 Insurance Charges Predictor")
st.write("Estimate medical insurance charges based on demographics and lifestyle.")

# User input
age = st.slider("Age", 18, 65, 30)
sex = st.selectbox("Sex", ["male", "female"])
bmi = st.number_input("BMI (Body Mass Index)", 10.0, 50.0, 25.0)
children = st.slider("Number of Children", 0, 5, 0)
smoker = st.selectbox("Smoker", ["yes", "no"])
region = st.selectbox("Region", ["northeast", "northwest", "southeast", "southwest"])

# Prepare input
input_dict = {
    'age': age,
    'bmi': bmi,
    'children': children,
    'sex_male': 1 if sex == 'male' else 0,
    'smoker_yes': 1 if smoker == 'yes' else 0,
    'region_northwest': 1 if region == 'northwest' else 0,
    'region_southeast': 1 if region == 'southeast' else 0,
    'region_southwest': 1 if region == 'southwest' else 0,
    'high_risk': int((smoker == 'yes') and (bmi > 30))
}

input_df = pd.DataFrame([input_dict])

# Prediction
if st.button("Predict Charges"):
    prediction = model.predict(input_df)[0]
    st.success(f"Estimated Insurance Charges: **${prediction:,.2f}**")
