import streamlit as st
import joblib
import pandas as pd

model = joblib.load("Model/model.pkl")

st.title("📚 Comic Rating Predictor")

year = st.number_input("Release Year", 1900, 2025)
pages = st.number_input("Page Count", 1, 5000)
volume = st.number_input("Volume Count", 1, 100)

format_ = st.selectbox("Format", ["Tankobon", "Graphic Novel"])
genre = st.selectbox("Genre", ["Action", "Romance", "Comedy"])

if st.button("Predict"):
    data = pd.DataFrame([{
        "Release Year": year,
        "Page Count": pages,
        "Volume Count": volume,
        "Format": format_,
        "Theme (Color Style)": "Black & White",
        "Genre": genre,
        "Country of Origin": "Japan",
        "Status": "Ongoing",
        "Language": "Japanese",
        "Age Rating": "Teen"
    }])

    pred = model.predict(data)
    st.success(f"Predicted Rating: {pred[0]:.2f}")