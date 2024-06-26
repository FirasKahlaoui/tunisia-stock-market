from flask import Flask, request, jsonify
from flask_cors import CORS
import numpy as np
import pickle

app = Flask(__name__)
CORS(app)

# Load your trained model
model = pickle.load(open('model.pkl', 'rb'))
scaler_features = pickle.load(open('scaler.pkl', 'rb'))
target_scaler = pickle.load(open('target_scaler.pkl', 'rb'))


@app.route('/predict', methods=['POST'])
def predict():
    data = request.json
    # Extract features from the request data
    features = np.array([
        data['openingPrice'],
        data['highestPrice'],
        data['lowestPrice'],
        data['volume'],
    ]).reshape(1, -1)
    
    # Scale the input features
    features_scaled = scaler_features.transform(features)

    # Predict the closing price
    prediction_scaled = model.predict(features_scaled)
    
    # Unscale the predicted closing price
    prediction_unscaled = target_scaler.inverse_transform(prediction_scaled.reshape(1,-1))

    response = {
        'closingPrice': prediction_unscaled[0][0]
    }
    return jsonify(response)

if __name__ == '__main__':
    app.run(debug=True)