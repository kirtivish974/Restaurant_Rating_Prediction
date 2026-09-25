import streamlit as st
import pandas as pd
import numpy as np
import pickle

st.set_page_config(page_title="Restaurant Rating Predictor", layout="centered")

@st.cache_resource
def load_model():
    with open('rf_model.pkl', 'rb') as f:
        data = pickle.load(f)
    return data['model'], data['columns']

model, feature_cols = load_model()

st.title("🍽️ Restaurant Rating Predictor")
st.write("Enter restaurant details to predict the aggregate rating.")

col1, col2 = st.columns(2)

with col1:
    price = st.slider("Price range", 1, 4, 2)
    cost = st.number_input("Average Cost for two", 0, 10000, 500, step=50)
    votes = st.number_input("Votes", 0, 20000, 100, step=10)
    country = st.number_input("Country Code", 1, 250, 1)
    cuisine_count = st.slider("Number of cuisines", 1, 8, 2)

with col2:
    table = st.selectbox("Has Table booking", ["Yes", "No"])
    online = st.selectbox("Has Online delivery", ["Yes", "No"])
    long = st.number_input("Longitude", -180.0, 180.0, 77.2, format="%.6f")
    lat = st.number_input("Latitude", -90.0, 90.0, 28.6, format="%.6f")

if st.button("🔮 Predict Rating", use_container_width=True):
    row = {c: 0 for c in feature_cols}
    row['Price range'] = price
    row['Average Cost for two'] = cost
    row['Votes'] = votes
    row['Country Code'] = country
    row['Cuisine Count'] = cuisine_count
    row['Longitude'] = long
    row['Latitude'] = lat

    if 'Has Table booking_Yes' in row:
        row['Has Table booking_Yes'] = 1 if table == "Yes" else 0
    if 'Has Table booking_No' in row:
        row['Has Table booking_No'] = 1 if table == "No" else 0
    if 'Has Online delivery_Yes' in row:
        row['Has Online delivery_Yes'] = 1 if online == "Yes" else 0
    if 'Has Online delivery_No' in row:
        row['Has Online delivery_No'] = 1 if online == "No" else 0

    X_input = pd.DataFrame([row])[feature_cols]
    pred = model.predict(X_input)[0]

    st.success(f"### Predicted Rating: ⭐ {pred:.2f} / 5")
    st.caption("Model: Random Forest Regressor (R² ≈ 0.58)")