import streamlit as st
import requests
import random

 # Change this URL to the one of your API
#API_URL = "http://localhost:8000"
API_URL = "https://api-nutrimap-1002154750813.europe-west1.run.app/"

st.title("Dummy Model - Flowers")

st.write("Nutrimap test - this is currently only the flower example")

sepal_length = st.slider('Select a value A', min_value=0, max_value=4, value=1, step=1)
sepal_width = st.slider('Select a value B',  min_value=0, max_value=4, value=1, step=1)
petal_length = st.slider('Select a value C',  min_value=0, max_value=4, value=1, step=1)
petal_width = st.slider('Select a value D',  min_value=0, max_value=4, value=1, step=1)

url = f"{API_URL}/predict"
params = {
    'sepal_length': sepal_length,
    'sepal_width': sepal_width,
    'petal_length': petal_length,
    'petal_width': petal_width,
}

response = requests.get(url, params=params).json()

st.write(f"This flower belongs to category {str(response['prediction'])}")


st.title("NutriMap - V1")

st.write("Nutrimap test - currently not connected to anything")

st.write("Select your main ingredients from the dropdowns below:")

# Define ingredient lists once
protein_list = [
    "Chicken Breast", "Tofu", "Lentils", "Eggs", "Greek Yogurt",
    "Salmon", "Beans", "Cottage Cheese"
]

carb_list = [
    "Rice", "Pasta", "Quinoa", "Potatoes", "Oats",
    "Wholegrain Bread", "Couscous", "Sweet Potato"
]

fat_list = [
    "Olive Oil", "Avocado", "Nuts", "Seeds",
    "Butter", "Cheese", "Tahini", "Peanut Butter"
]

# Dropdowns
protein_option = st.selectbox(
    "Select your source of protein",
    protein_list
)

carb_option = st.selectbox(
    "Select your source of carbs",
    carb_list
)

fat_option = st.selectbox(
    "Select your source of fats",
    fat_list
)

st.write("Your dish consists of:", protein_option, carb_option, fat_option)

# Pick random "improved" suggestions
suggested_protein = random.choice(protein_list)
suggested_carb = random.choice(carb_list)
suggested_fat = random.choice(fat_list)

# Display recommendation
st.write(
    f"Switching to **{suggested_protein}**, **{suggested_carb}** and **{suggested_fat}** "
    f"would improve your diet significantly."
)
