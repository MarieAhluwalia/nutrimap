import streamlit as st
import requests
import random
import time

# --- PAGE CONFIG ---
st.set_page_config(page_title="NutriMap Demo", layout="centered")

# --- GREEN BUTTON ONLY (NO GLOBAL BACKGROUND/TEXT CHANGES) ---
st.markdown(
    """
    <style>
    .stButton > button {
        background-color: #22a34f;
        color: white;
        border-radius: 8px;
        border: none;
        padding: 0.4rem 0.9rem;
    }
    .stButton > button:hover {
        background-color: #1b7c3a;
        color: white;
    }
    </style>
    """,
    unsafe_allow_html=True,
)

API_URL = "https://api-nutrimap-1002154750813.europe-west1.run.app/"

st.title("NutriMap Demo")

st.markdown(
    "Below you find a small demo: on top the old flower test model, "
    "followed by the first NutriMap V1 ingredient selector."
)

# ==========================================
# DEV / DEBUG SECTION – OLD FLOWER MODEL
# ==========================================
with st.expander("🔬 Dummy Model – Flowers (dev only)"):
    st.caption("Legacy Iris model for API testing. Not part of the NutriMap UI.")

    sepal_length = st.slider("Select a value A", min_value=0, max_value=4, value=1, step=1)
    sepal_width = st.slider("Select a value B", min_value=0, max_value=4, value=1, step=1)
    petal_length = st.slider("Select a value C", min_value=0, max_value=4, value=1, step=1)
    petal_width = st.slider("Select a value D", min_value=0, max_value=4, value=1, step=1)

    url = f"{API_URL}/predict"
    params = {
        "sepal_length": sepal_length,
        "sepal_width": sepal_width,
        "petal_length": petal_length,
        "petal_width": petal_width,
    }

    try:
        response = requests.get(url, params=params, timeout=3).json()
        st.success(f"This flower belongs to category **{str(response['prediction'])}**")
    except Exception:
        st.warning("Backend not reachable – expected for this demo.")

# ==========================================
# MAIN SECTION – NUTRIMAP V1
# ==========================================
st.markdown("---")
st.header("🍽️ NutriMap – V1 Prototype")
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

# Layout: left = inputs + button, right = summary & suggestion
col_left, col_right = st.columns([2, 1])

with col_left:
    protein_option = st.selectbox("🥩 Protein source", protein_list)
    carb_option = st.selectbox("🍞 Carb source", carb_list)
    fat_option = st.selectbox("🥑 Fat source", fat_list)

    calculate = st.button("Calculate better alternatives")

with col_right:
    st.subheader("Your dish")
    st.markdown(
        f"- **Protein:** {protein_option}  \n"
        f"- **Carbs:** {carb_option}  \n"
        f"- **Fats:** {fat_option}"
    )

    if calculate:
        with st.spinner("Calculating better alternatives..."):
            time.sleep(1.5)  # simulate processing delay

            suggested_protein = random.choice(protein_list)
            suggested_carb = random.choice(carb_list)
            suggested_fat = random.choice(fat_list)

        st.subheader("Suggested improvement")
        st.success(
            f"Better alternatives could be **{suggested_protein}** as protein, "
            f"**{suggested_carb}** as carbs and **{suggested_fat}** as fats."
        )

st.markdown("---")
st.caption("NutriMap V1 prototype – backend not connected yet.")
