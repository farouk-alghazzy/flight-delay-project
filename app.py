
import streamlit as st
import pandas as pd
import numpy as np
import joblib

st.set_page_config(page_title="Flight Delay Predictor", page_icon="✈️")

st.title("✈️ Flight Delay Prediction App")
st.write("""
Welcome!  
This app predicts whether a flight will be **delayed** or **on time** based on flight details such as departure delay, flight distance, and air time.

- Fill in the flight information under the "Flight Prediction" tab.
- Explore flight delay patterns in the "Visualizations" tab.
""")

best_rf_model = joblib.load("outputs/best_rf_model.pkl")

tab1, tab2 = st.tabs(["✈️ Flight Prediction", "📊 Visualizations"])

with tab1:
    st.header("Enter Flight Details:")

    dep_delay = st.number_input("Departure Delay (minutes)", min_value=0, value=0)
    distance = st.number_input("Distance (miles)", min_value=0, value=500)
    air_time = st.number_input("Air Time (minutes)", min_value=0, value=100)

    if st.button("Predict Delay Status", key="predict_button"):
        input_features = np.array([[dep_delay, distance, air_time]])
        prediction = best_rf_model.predict(input_features)[0]

        if prediction == 1:
            st.error("Prediction: Delayed 🛬")
        else:
            st.success("Prediction: On Time 🛫")

with tab2:
    st.header("Visualizations")
    st.image("outputs/figures/avg_delay_by_airline.png")
    st.image("outputs/figures/total_delay_by_cause.png")
    st.image("outputs/figures/cancellation_rate_by_airline.png")



