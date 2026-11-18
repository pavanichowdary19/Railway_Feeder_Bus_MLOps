
# Railway Feeder Bus Connection Prediction - MLOps Project

## Project Overview
This project predicts whether railway passengers may miss their feeder bus connections.

## Objectives
- Generate synthetic datasets.
- Perform data preprocessing.
- Perform feature engineering.
- Store reusable features using Feast.
- Train Decision Tree and Gradient Boosting models.
- Track experiments using MLflow.
- Automate testing using GitHub Actions.
- Deploy predictions using FastAPI.

## Dataset
- Version 1: Normal railway conditions (300 records).
- Version 2: Peak-hour conditions (300 records).

## Feature Engineering
- estimated_walking_time
- transfer_time_margin

## Machine Learning Models
- Decision Tree Classifier
- Gradient Boosting Classifier

Selected Model: Gradient Boosting

## MLflow
Registered Model: RailwayConnectionRiskModel
Version: 1

## Model Evaluation
- Accuracy: 90.0%
- Precision: 93.2%
- Recall: 90.8%
- F1 Score: 92.0%

## Automated Testing
Five automated tests passed successfully.

## FastAPI
Endpoints:
- GET /
- POST /predict

Prediction results:
- Connection Likely
- Connection at Risk

## Final Result
The FastAPI prediction endpoint returned HTTP status code 200.
