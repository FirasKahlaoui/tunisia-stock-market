from flask import Flask, request, jsonify
from flask_cors import CORS
import numpy as np
import pickle

app = Flask(__name__)
CORS(app)

# Load your trained model
model = pickle.load(open('stock_model.pkl', 'rb'))

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
    
    # Predict the closing price
    prediction = model.predict(features)
    response = {
        'closingPrice': prediction[0],
        'additionalInfo': 'Example additional information'
    }
    return jsonify(response)

if __name__ == '__main__':
    app.run(debug=True)
