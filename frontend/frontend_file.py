import streamlit as st
import requests

 # Change this URL to the one of your API
API_URL = "https://my-api-app-1234567891234.europe-west1.run.app/"

st.title("My awesome MVP")

st.write("Nutrimap predictor")

sepal_length = st.slider('Select a value for Sepal length', min_value=0, max_value=4, value=1, step=1)
sepal_width = st.slider('Select a value for Sepal width',  min_value=0, max_value=4, value=1, step=1)
petal_length = st.slider('Select a value for Petal length',  min_value=0, max_value=4, value=1, step=1)
petal_width = st.slider('Select a value for Petal width',  min_value=0, max_value=4, value=1, step=1)

url = f"{API_URL}/predict"
params = {
    'sepal_length': sepal_length,
    'sepal_width': sepal_width,
    'petal_length': petal_length,
    'petal_width': petal_width,
}

response = requests.get(url, params=params).json()

st.write(f"This flower belongs to category {str(response['prediction'])}")
