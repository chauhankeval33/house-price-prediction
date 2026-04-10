import streamlit as st
import joblib
import pandas as pd

# Load model
model = joblib.load("house_price_model.pkl")

# Page config
st.set_page_config(page_title="House Price Predictor", layout="wide")

# -------- SIDEBAR -------- #
st.sidebar.title("🏠 Input Features")

longitude = st.sidebar.number_input("Longitude", value=-122.23)
latitude = st.sidebar.number_input("Latitude", value=37.88)
housing_median_age = st.sidebar.slider("House Age", 1, 100, 41)

total_rooms = st.sidebar.number_input("Total Rooms", value=880)
total_bedrooms = st.sidebar.number_input("Total Bedrooms", value=129)
population = st.sidebar.number_input("Population", value=322)
households = st.sidebar.number_input("Households", value=126)
median_income = st.sidebar.number_input("Median Income", value=8.32)

ocean_proximity = st.sidebar.selectbox(
    "Ocean Proximity",
    ["<1H OCEAN", "INLAND", "NEAR OCEAN", "NEAR BAY", "ISLAND"]
)

# -------- MAIN PAGE -------- #
st.title("🏡 House Price Prediction App")
st.markdown("### Enter details in sidebar and click predict")

# Show location on map
map_data = pd.DataFrame({
    "lat": [latitude],
    "lon": [longitude]
})
st.map(map_data)

# Feature Engineering
rooms_per_household = total_rooms / households if households != 0 else 0
bedrooms_per_room = total_bedrooms / total_rooms if total_rooms != 0 else 0
population_per_household = population / households if households != 0 else 0

# Display inputs nicely
st.subheader("📊 Input Summary")
st.write({
    "Longitude": longitude,
    "Latitude": latitude,
    "Rooms": total_rooms,
    "Bedrooms": total_bedrooms,
    "Population": population,
    "Income": median_income,
    "Ocean": ocean_proximity
})

# Predict
if st.button("💰 Predict Price"):
    input_data = pd.DataFrame([{
        "longitude": longitude,
        "latitude": latitude,
        "housing_median_age": housing_median_age,
        "total_rooms": total_rooms,
        "total_bedrooms": total_bedrooms,
        "population": population,
        "households": households,
        "median_income": median_income,
        "ocean_proximity": ocean_proximity,
        "rooms_per_household": rooms_per_household,
        "bedrooms_per_room": bedrooms_per_room,
        "population_per_household": population_per_household
    }])

    prediction = model.predict(input_data)

    st.success(f"🏡 Estimated Price: ₹ {prediction[0]:,.2f}")

    st.balloons()