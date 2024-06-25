from flask import Flask, request, jsonify
from flask_cors import CORS
import numpy as np
import pickle

# Load your trained model
model = pickle.load(open('backend/test_model.pkl', 'rb'))
scaler = pickle.load(open('backend/scaler.pkl', 'rb'))
target_scaler = pickle.load(open('backend/target_scaler.pkl', 'rb'))

# Sample input data for testing
data = {
    'openingPrice': 23.63,
    'highestPrice': 23.63,
    'lowestPrice': 22.75,
    'volume': 1608
}

features = np.array([[data['openingPrice'], data['highestPrice'], data['lowestPrice'], data['volume']]]).reshape(1, -1)

data_scaled = scaler.transform(features)
print("Scaled Data:", data_scaled)

# Predict the closing price using the scaled features
data_prediction = model.predict(data_scaled)
print("Predicted Scaled Closing Price:", data_prediction)

# Unscale the predicted closing price
prediction_unscaled = target_scaler.inverse_transform(data_prediction.reshape(-1, 1))
print("Unscaled Prediction:", prediction_unscaled)

response = {
    'closingPrice': prediction_unscaled[0][0]
}

print(response)





