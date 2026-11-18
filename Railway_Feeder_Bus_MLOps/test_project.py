
import joblib
import pandas as pd
from fastapi.testclient import TestClient
from app import app

# Load the saved model
model = joblib.load("/content/railway_connection_model.pkl")

client = TestClient(app)


def calculate_transfer_margin(scheduled_time, train_delay, walking_time):
    return scheduled_time - train_delay - walking_time


# Test 1: Transfer margin calculation
def test_transfer_margin():
    assert calculate_transfer_margin(20, 5, 8) == 7


# Test 2: Negative transfer margin
def test_negative_margin():
    assert calculate_transfer_margin(10, 8, 5) == -3


# Test 3: Model prediction
def test_model_prediction():
    sample = pd.DataFrame([{
        "train_delay_min": 12,
        "distance_m": 300,
        "walking_speed_mps": 1.0,
        "crowd_density": "High",
        "luggage_category": "Heavy",
        "scheduled_transfer_min": 10,
        "lift_escalator_available": "No",
        "estimated_walking_time": 13,
        "transfer_time_margin": -15,
        "dataset_version": "Version 2"
    }])

    prediction = model.predict(sample)
    assert prediction[0] in [0, 1]


# Test 4: API home endpoint
def test_api_home():
    response = client.get("/")
    assert response.status_code == 200


# Test 5: API prediction endpoint
def test_api_prediction():
    sample = {
        "train_delay_min": 12,
        "distance_m": 300,
        "walking_speed_mps": 1.0,
        "crowd_density": "High",
        "luggage_category": "Heavy",
        "scheduled_transfer_min": 10,
        "lift_escalator_available": "No",
        "estimated_walking_time": 13,
        "transfer_time_margin": -15,
        "dataset_version": "Version 2"
    }

    response = client.post("/predict", json=sample)

    assert response.status_code == 200
    assert response.json()["prediction"] in [0, 1]
