import tensorflow as tf
from tensorflow import keras
import pandas as pd
import numpy as np
import seaborn as sns
import matplotlib.pyplot as plt
from geopy.distance import geodesic
from tensorflow.keras.optimizers import Adam
from sklearn.model_selection import train_test_split
from sklearn.preprocessing import LabelEncoder, StandardScaler
from .preprocess import preprocess_data, split_and_encode
from tensorflow.keras.models import load_model

import joblib

rf_model = joblib.load('fraud_detection/ml_models/random_forest_model.pkl')
fnn_model = load_model('fraud_detection/ml_models/fnn_model.keras')
lr_model = joblib.load('fraud_detection/ml_models/logistic_regression_model.pkl')

def analyze_csv(file_path):
    # Preprocess file
    df = preprocess_data(file_path)
    X_train, X_val, X_test, y_train, y_val, y_test, label_encoded = split_and_encode(df)

    # Example: Predict using models (Random Forest, FNN, Logistic Regression)
    rf_predictions = rf_model.predict(X_test)
    fnn_predictions = fnn_model.predict(X_test)
    lr_predictions = lr_model.predict(X_test)

    # Combine model predictions (ensemble example)
    final_predictions = (rf_predictions + fnn_predictions + lr_predictions) / 3

    return rf_predictions