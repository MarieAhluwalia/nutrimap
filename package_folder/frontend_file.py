import streamlit as st
import requests

 # Change this URL to the one of your API
#API_URL = "http://localhost:8000"
API_URL = "https://api-nutrimap-1002154750813.europe-west1.run.app/"

st.title("NutriMap - Test")

st.write("Nutrimap test - ignore errors, backend is not properly configured :)")

sepal_length = st.slider('Select a value for Carbs', min_value=0, max_value=4, value=1, step=1)
sepal_width = st.slider('Select a value for Protein',  min_value=0, max_value=4, value=1, step=1)
petal_length = st.slider('Select a value for Total Fats',  min_value=0, max_value=4, value=1, step=1)
petal_width = st.slider('Select a value for Unsaturated Fats',  min_value=0, max_value=4, value=1, step=1)

url = f"{API_URL}/predict"
params = {
    'sepal_length': sepal_length,
    'sepal_width': sepal_width,
    'petal_length': petal_length,
    'petal_width': petal_width,
}

response = requests.get(url, params=params).json()

st.write(f"This flower belongs to category {str(response['prediction'])}")
