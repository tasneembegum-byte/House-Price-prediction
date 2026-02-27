import streamlit as st
import pickle
import numpy as np

# Load model
model = pickle.load(open("model.pkl", "rb"))

st.title("🏠 House Price Prediction App")

st.write("Enter House Details Below:")

# Taking all 7 inputs
area = st.number_input("Area (in square feet)")
bedrooms = st.number_input("Number of Bedrooms")
bathrooms = st.number_input("Number of Bathrooms")
floors = st.number_input("Number of Floors")
age = st.number_input("Age of House (years)")
garage = st.number_input("Garage (0 = No, 1 = Yes)")
location_score = st.number_input("Location Score (1-10)")

if st.button("Predict Price"):
    features = np.array([[area, bedrooms, bathrooms, floors, age, garage, location_score]])
    prediction = model.predict(features)

    st.success(f"Predicted House Price: ₹ {prediction[0]:,.2f}")
