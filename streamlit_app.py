import streamlit as st
import requests

# Page config
st.set_page_config(page_title="Iris Flower Prediction", page_icon="🌸", layout="centered")

# Header and title
st.title("🌼 Iris Flower Prediction 🌼")
st.markdown("Provide the dimensions of the iris flower to predict its species.")

# Dictionary for image paths
image_paths = {
    "setosa": "setosa.png",
    "versicolor": "versicolor.png",
    "virginica": "virginica.png"
}

# Sidebar inputs for Iris features and predict button
with st.sidebar:
    st.header("Input Features")
    sepal_length = st.number_input("Sepal Length", min_value=0.0, max_value=10.0, value=5.1)
    sepal_width = st.number_input("Sepal Width", min_value=0.0, max_value=10.0, value=3.5)
    petal_length = st.number_input("Petal Length", min_value=0.0, max_value=10.0, value=1.4)
    petal_width = st.number_input("Petal Width", min_value=0.0, max_value=10.0, value=0.2)

    # Button remains in the sidebar
    if st.button("Predict 🌿"):
        # Use the FastAPI URL running locally
        api_url = "http://localhost:8000/predict/"
        
        payload = {
            "sepal_length": sepal_length,
            "sepal_width": sepal_width,
            "petal_length": petal_length,
            "petal_width": petal_width
        }
        
        # Make the POST request to the FastAPI backend
        response = requests.post(api_url, json=payload)

        if response.status_code == 200:
            prediction = response.json().get("prediction", "Error in prediction")
            st.session_state.prediction = prediction
        else:
            st.session_state.prediction = "⚠️ Error: Unable to fetch prediction"

# Show prediction and display the associated image
if "prediction" in st.session_state:
    prediction = st.session_state.prediction
    if prediction in image_paths:
        st.success(f"🌷 The predicted Iris species is: {prediction.capitalize()}")
        st.image(image_paths[prediction], caption=f"Iris {prediction.capitalize()}", use_column_width=True)
    else:
        st.error("⚠️ Unknown species predicted or issue with prediction.")

# Footer
st.markdown("---")
st.markdown("Developed with ❤️ using FastAPI and Streamlit")
