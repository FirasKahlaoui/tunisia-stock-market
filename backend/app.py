from flask import Flask, request, jsonify
from tensorflow.keras.models import load_model
import numpy as np
import json

app = Flask(__name__)

# Load your trained model
model = load_model('../notebooks/models/stock_price_prediction.h5')

# Load the scaler (assuming you saved it using joblib)
from sklearn.preprocessing import MinMaxScaler
import joblib
scaler = joblib.load('./scaler.pkl')

@app.route('/predict', methods=['POST'])
def predict():
    data = request.json
    input_data = np.array(data['input']).reshape(1, -1)
    scaled_data = scaler.transform(input_data)
    scaled_data = scaled_data.reshape((1, len(data['input']), 1))
    
    prediction = model.predict(scaled_data)
    prediction = scaler.inverse_transform(prediction)
    
    return jsonify({'prediction': prediction[0][0]})

if __name__ == '__main__':
    app.run(debug=True)
