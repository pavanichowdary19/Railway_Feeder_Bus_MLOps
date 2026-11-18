
from fastapi import FastAPI
from pydantic import BaseModel
import joblib
import pandas as pd

app = FastAPI(
    title="Railway Feeder Bus Connection Prediction API",
    description="Predicts whether passengers may miss feeder bus connections",
    version="1.0"
)

# Load trained model
model = joblib.load("/content/railway_connection_model.pkl")


class TransferInput(BaseModel):
    train_delay_min: int
    distance_m: int
    walking_speed_mps: float
    crowd_density: str
    luggage_category: str
    scheduled_transfer_min: int
    lift_escalator_available: str
    estimated_walking_time: float
    transfer_time_margin: float
    dataset_version: str


@app.get("/")
def home():
    return {"message": "Railway Connection Prediction API is running"}


@app.post("/predict")
def predict_connection(data: TransferInput):

    input_data = pd.DataFrame([data.model_dump()])

    prediction = model.predict(input_data)[0]

    if prediction == 1:
        result = "Connection at Risk"
    else:
        result = "Connection Likely"

    return {
        "prediction": int(prediction),
        "connection_status": result
    }
