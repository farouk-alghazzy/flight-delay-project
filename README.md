# ✈️ Flight Delay Prediction Project

This project explores flight delay patterns and builds a model to predict whether a flight will arrive on time or not, using a 3-million-row dataset from the U.S. Department of Transportation (2019–2023).

## 📦 Dataset
- Source: [Kaggle - Flight Delay and Cancellation Dataset (2019–2023)](https://www.kaggle.com/datasets/patrickz/flight-delay-and-cancellation-20192023)
- Size: 3,000,000 rows
- Features include: flight date, airline, origin/destination airports, scheduled and actual times, delays, cancellations, and delay causes.

## 🧪 Exploratory Data Analysis
- Checked for missing values
- Visualized average delays by airline and airport
- Explored cancellation rates and causes
- Identified most important features for delay prediction

## 🤖 Modeling 
- Logistic Regression and Random Forest classifiers
- Target variable: **On Time vs Delayed** (e.g. `ARR_DELAY` ≥ 15 min = Delayed)
- Accuracy, precision, recall evaluation

## 🛠 Tools Used
- Python, Pandas, Matplotlib, Seaborn
- Scikit-learn
- Jupyter Notebook
---
