from fastapi import FastAPI
import pickle

from package_folder.iris import my_prediction_function

# FastAPI instance
app = FastAPI()

# Root endpoint
@app.get("/")
def root():
    return {'greeting':"hello"}

# Prediction endpoint
@app.get("/predict")
def predict(sepal_length, sepal_width, petal_length, petal_width):
    # Use the function in our package to run the prediction
    prediction = my_prediction_function(sepal_length, sepal_width, petal_length, petal_width)

    # Return prediction
    return {"prediction": int(prediction[0])}
