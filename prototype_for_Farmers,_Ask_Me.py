import streamlit as st
from google.oauth2 import service_account
import os
from PIL import Image
import numpy as np
import model  
from utils import get_weather_info, get_news, calculate_land_size


def user_login():
    st.write("User Login Placeholder (implement Google OAuth)")


def main():
    st.title("FARMER, ASK ME")
    user_login()
    
    menu = ["Home", "Disease Detection", "Farming Guide", "Weather Updates", "News", "Land Size Calculator"]
    choice = st.sidebar.selectbox("Select Feature", menu)

    if choice == "Home":
        st.image("background.jpg")  # Placeholder for a background image
        st.write("Welcome to Farmer, Ask Me!")
        st.write("Your AI companion for effective farming.")

    elif choice == "Disease Detection":
        st.subheader("Upload Plant Image for Diagnosis")
        uploaded_file = st.file_uploader("Choose an image...", type=["jpg", "jpeg", "png"])
        
        if uploaded_file is not None:
            image = Image.open(uploaded_file)
            st.image(image, caption='Uploaded Image.', use_column_width=True)
            diagnosis, treatment = model.predict_disease(image)
            st.write(f"Diagnosis: {diagnosis}")
            st.write("Recommended Treatment Options:")
            st.write(treatment)

    elif choice == "Farming Guide":
        st.subheader("Farmers Ask Me (FAM)")
        st.write("Ask your farming-related questions:")
        question = st.text_input("Enter your question:")
        if st.button("Ask"):
            # Simulate response
            st.write("This feature will provide you with answers based on farming knowledge.")

    elif choice == "Weather Updates":
        st.subheader("Current Weather and Forecast")
        weather_info = get_weather_info()
        st.write(weather_info)

    elif choice == "News":
        st.subheader("Latest Agricultural News")
        news_articles = get_news()
        for article in news_articles:
            st.write(article)

    elif choice == "Land Size Calculator":
        st.subheader("Calculate Your Land Size")
        length = st.number_input("Enter Length (in meters):", min_value=0.0)
        width = st.number_input("Enter Width (in meters):", min_value=0.0)
        if st.button("Calculate"):
            area = calculate_land_size(length, width)
            st.write(f"Total Land Area: {area} square meters")

if __name__ == '__main__':
    main()



# model
import numpy as np

def predict_disease(image):
    # Dummy implementation for demonstration
    diagnosis = "Fungal Infection"  # Placeholder for actual model prediction
    treatment = {
        "Organic": "Neem oil spray.",
        "Chemical": "Fungicide X."
    }
    return diagnosis, treatment


#utils
def get_weather_info():
    # Placeholder for actual weather data retrieval
    return "Sunny, 25°C with a chance of rain."

def get_news():
    # Placeholder for news articles
    return [
        "New pesticide approved for use against crop diseases.",
        "Market prices for corn are on the rise."
    ]

def calculate_land_size(length, width):
    return length * width
