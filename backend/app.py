from flask import Flask, request, jsonify
from tensorflow.keras.models import load_model # type: ignore
import numpy as np
import joblib
from sklearn.preprocessing import MinMaxScaler

app = Flask(__name__)

# Load your trained model
model = load_model('../notebooks/models/stock_price_prediction.h5')

# Load the scaler (make sure this scaler matches your model training)
scaler = joblib.load('../notebooks/models/scaler.pkl')

@app.route('/predict', methods=['POST'])
def predict():
    try:
        data = request.json
        
        # Ensure 'input' is in the correct format
        if 'input' not in data or not isinstance(data['input'], list): # type: ignore
            return jsonify({'error': 'Invalid input data. Expected a list of values.'}), 400
        
        # Convert input data to numpy array and reshape
        input_data = np.array(data['input']) # type: ignore
        
        # Check the input shape
        if input_data.shape[0] != scaler.n_features_in_:
            return jsonify({'error': f'Expected {scaler.n_features_in_} features, but got {input_data.shape[0]} features.'}), 400
        
        input_data = input_data.reshape(1, -1)
        
        # Scale the input data
        scaled_data = scaler.transform(input_data)
        
        # Reshape for the model input
        scaled_data = scaled_data.reshape((1, scaled_data.shape[1], 1))
        
        # Predict using the model
        prediction = model.predict(scaled_data)
        
        # Assuming the scaler was fitted only on the target variable, you might not need to unscale the prediction
        # If needed, you should have a separate scaler for the target variable.
        # prediction = target_scaler.inverse_transform(prediction)
        
        return jsonify({'prediction': float(prediction[0][0])})

    except Exception as e:
        return jsonify({'error': str(e)}), 500

if __name__ == '__main__':
    app.run(debug=True)
