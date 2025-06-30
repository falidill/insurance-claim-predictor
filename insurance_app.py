import streamlit as st
import pandas as pd
import numpy as np
from sklearn.ensemble import GradientBoostingRegressor
from sklearn.model_selection import train_test_split

# App title and description
st.title("💸 Insurance Charges Predictor")
st.write("Estimate medical insurance charges based on demographics and lifestyle.")

# Cache the model training function
@st.cache_resource
def train_model():
    df = pd.read_csv("insurance.csv")
    df = pd.get_dummies(df, columns=['sex', 'smoker', 'region'], drop_first=True)
    df['high_risk'] = ((df['smoker_yes'] == 1) & (df['bmi'] > 30)).astype(int)

    X = df.drop('charges', axis=1)
    y = df['charges']

    X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2, random_state=42)
    model = GradientBoostingRegressor(random_state=42)
    model.fit(X_train, y_train)

    return model

model = train_model()

# Sidebar inputs
st.sidebar.header("Enter Input Values")

age = st.sidebar.slider("Age", 18, 65, 30)
sex = st.sidebar.selectbox("Sex", ["male", "female"])
bmi = st.sidebar.number_input("BMI (Body Mass Index)", 10.0, 50.0, 25.0)
children = st.sidebar.slider("Number of Children", 0, 5, 0)
smoker = st.sidebar.selectbox("Smoker", ["yes", "no"])
region = st.sidebar.selectbox("Region", ["northeast", "northwest", "southeast", "southwest"])

# Prepare input for model
input_data = {
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

input_df = pd.DataFrame([input_data])

# Prediction
if st.button("Predict Charges"):
    prediction = model.predict(input_df)[0]
    st.success(f"Estimated Insurance Charges: **${prediction:,.2f}**")
