from fastapi import FastAPI
from pydantic import BaseModel
import joblib
import numpy as np
from sklearn.datasets import load_iris

app = FastAPI()

# Load the Iris dataset target names for decoding predictions
iris = load_iris()

# Load the trained model and scaler
try:
    model = joblib.load('logistic_regression_model.pkl')
    scaler = joblib.load('scaler.pkl')
except Exception as e:
    print(f"Error loading model or scaler: {e}")

class IrisFeatures(BaseModel):
    sepal_length: float
    sepal_width: float
    petal_length: float
    petal_width: float

@app.get("/")
def read_root():
    return {"message": "Welcome to the Iris prediction API"}

@app.post("/predict/")
def predict_iris(features: IrisFeatures):
    try:
        # Prepare the input data for the model
        input_data = np.array([[features.sepal_length, features.sepal_width, features.petal_length, features.petal_width]])
        
        # Scale the input data
        input_data = scaler.transform(input_data)
        
        # Make the prediction
        prediction = model.predict(input_data)
        
        # Get the predicted class name
        predicted_class = iris.target_names[prediction[0]]
        
        # Return the prediction
        return {"prediction": predicted_class}
    except Exception as e:
        print(f"Error during prediction: {e}")
        return {"error": "Internal server error"}, 500
