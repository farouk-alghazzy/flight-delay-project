
import streamlit as st
import warnings
import joblib
warnings.filterwarnings("ignore")

best_rf_model = joblib.load("outputs/best_rf_model.pkl")
st.title("Flight Delay Prediction App")

st.write("""
This app predicts whether a flight will be **delayed** based on flight features like departure delay, distance, and air time.
""")

st.header("Enter Flight Details:")

dep_delay = st.number_input("Departure Delay (minutes)", min_value=0, max_value=300, value=0)
distance = st.number_input("Distance (miles)", min_value=1, max_value=5000, value=500)
air_time = st.number_input("Air Time (minutes)", min_value=1, max_value=1000, value=100)

if st.button("Predict Delay Status"):
    input_features = [[dep_delay, distance, air_time]]
    prediction = best_rf_model.predict(input_features)[0]

    if prediction == 1:
        st.error("Prediction: Delayed")
    else:
        st.success("Prediction: On Time")



