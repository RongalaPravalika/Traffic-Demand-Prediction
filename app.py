import streamlit as st
import pandas as pd
import joblib

# Load trained model
model = joblib.load("traffic_demand_model.pkl")

st.set_page_config(page_title="Traffic Demand Prediction")

st.title("🚦 Traffic Demand Prediction System")

st.write("Enter traffic details and predict demand.")

geohash = st.number_input("Geohash Encoded Value", value=0)

day = st.number_input("Day", min_value=1, max_value=365, value=48)

roadtype = st.number_input("RoadType Encoded Value", value=0)

lanes = st.number_input("Number of Lanes", min_value=1, value=1)

largevehicles = st.number_input("LargeVehicles Encoded Value", value=0)

landmarks = st.number_input("Landmarks Encoded Value", value=0)

temperature = st.number_input("Temperature", value=25.0)

weather = st.number_input("Weather Encoded Value", value=0)

hour = st.number_input("Hour", min_value=0, max_value=23, value=12)

minute = st.number_input("Minute", min_value=0, max_value=59, value=0)

if st.button("Predict Demand"):

    data = pd.DataFrame([[

        geohash,
        day,
        roadtype,
        lanes,
        largevehicles,
        landmarks,
        temperature,
        weather,
        hour,
        minute

    ]], columns=[

        'geohash',
        'day',
        'RoadType',
        'NumberofLanes',
        'LargeVehicles',
        'Landmarks',
        'Temperature',
        'Weather',
        'hour',
        'minute'

    ])

    prediction = model.predict(data)

    st.success(f"Predicted Demand: {prediction[0]:.4f}")