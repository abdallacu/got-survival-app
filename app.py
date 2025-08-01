# -*- coding: utf-8 -*-
"""app

Automatically generated by Colab.

Original file is located at
    https://colab.research.google.com/drive/1x6OwWFfdI3Z08FrjtRRQdAFOEyFDXDZw
"""

# app.py
import streamlit as st
import numpy as np
import joblib

# Load model and scaler
model = joblib.load("model.pkl")
scaler = joblib.load("scaler.pkl")

st.title("Game of Thrones Character Survival Predictor")

st.write("Enter the character features below:")

# Input fields
pred = st.selectbox("Prediction Source (0 = unknown, 1 = known)", [0, 1])
alive = st.selectbox("Alive at some point (0 = No, 1 = Yes)", [0, 1])
plod = st.selectbox("Plod (0 = No, 1 = Yes)", [0, 1])
male = st.selectbox("Gender (0 = Female, 1 = Male)", [0, 1])
house = st.number_input("House (encoded)", min_value=0, max_value=100, step=1)
book1 = st.selectbox("Appears in Book 1", [0, 1])
book2 = st.selectbox("Appears in Book 2", [0, 1])
book3 = st.selectbox("Appears in Book 3", [0, 1])
book4 = st.selectbox("Appears in Book 4", [0, 1])
book5 = st.selectbox("Appears in Book 5", [0, 1])
isMarried = st.selectbox("Is Married (0 = No, 1 = Yes)", [0, 1])
isNoble = st.selectbox("Is Noble (0 = No, 1 = Yes)", [0, 1])
numDeadRelations = st.number_input("Number of Dead Relations", min_value=0, max_value=100, step=1)
boolDeadRelations = st.selectbox("Has Dead Relations (0 = No, 1 = Yes)", [0, 1])
isPopular = st.selectbox("Is Popular (0 = No, 1 = Yes)", [0, 1])
popularity = st.slider("Popularity Score", 0.0, 1.0, 0.5)

# Arrange features in the correct order
features = np.array([[pred, alive, plod, male, house, book1, book2, book3,
                      book4, book5, isMarried, isNoble, numDeadRelations,
                      boolDeadRelations, isPopular, popularity]])

# Scale input
features_scaled = scaler.transform(features)

# Predict
if st.button("Predict"):
    prediction = model.predict(features_scaled)[0]
    st.success(f"Prediction: {'Alive' if prediction == 1 else 'Dead'}")
