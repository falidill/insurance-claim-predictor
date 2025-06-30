Streamlit app for predicting insurance claim charges using Gradient Boosting
# 💸 Insurance Charges Predictor

This Streamlit app predicts individual medical insurance charges based on user demographics and lifestyle data using a machine learning model.

🟢 **Live App**: [Click here to try it out](https://insurance-claim-predictor-8ep2mqqchbn4gxasgpz53d.streamlit.app/))

---

## 📌 Project Overview

Healthcare costs can be difficult to anticipate. This app helps simulate how factors like **age**, **BMI**, **smoking habits**, and **region** affect insurance premiums using a **Gradient Boosting Regressor** trained on real data.

It’s a simplified version of how actuaries and pricing analysts estimate individual risk — brought to life using Python and Streamlit.

---

## 🧠 Features

- Interactive sliders and dropdowns for input
- Real-time prediction of insurance charges
- Feature engineering: creates a `high_risk` indicator for smokers with high BMI
- Trained on the [Kaggle Medical Cost dataset](https://www.kaggle.com/datasets/mirichoi0218/insurance)

---

## ⚙️ How It Works

1. Loads `insurance.csv`
2. One-hot encodes categorical features
3. Adds a custom `high_risk` feature
4. Trains a **Gradient Boosting Regressor** on-the-fly (to avoid .pkl issues)
5. Accepts user input → returns predicted insurance charges instantly

---

## 🛠️ Tech Stack

- Python
- Streamlit
- Pandas & NumPy
- Scikit-learn (GradientBoostingRegressor)

---

## 📁 File Structure
📦 insurance-claim-predictor
│
├── insurance_app.py # Streamlit app
├── insurance.csv # Dataset
├── requirements.txt # Dependencies for Streamlit Cloud
└── README.md # This file


---

## 🙋🏽‍♀️ About Me

Hi, I’m Fali Honutse — a Data Science graduate with a background in Actuarial Science, Finance, and Statistics. I love using data to make decision-making clearer and more human-centered.

💼 [LinkedIn](https://www.linkedin.com/in/fali-dillys-honutse)  
📬 [Portfolio] (https://falidill.github.io/portfolio-website/)) 

---

## 📝 License

This project is open-source and for educational/demo purposes.



