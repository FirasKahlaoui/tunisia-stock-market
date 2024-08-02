import streamlit as st
import requests
import json

st.title("Stock Price Prediction")

st.write("Input the last 20 days of stock prices to predict the next day's price.")

# Create input fields for the last 20 days' stock prices
input_data = []
for i in range(20):
    input_data.append(st.number_input(f"Day {i+1} Price", min_value=0.0, format="%.2f"))

# When the user clicks the button, send the input data to the Flask server
if st.button("Predict"):
    if len(input_data) == 20:
        input_data = [float(x) for x in input_data]
        data = {'input': input_data}
        response = requests.post('http://127.0.0.1:5000/predict', json=data)
        result = response.json()
        st.write(f"Predicted next day price: {result['prediction']:.2f}")
    else:
        st.write("Please enter all 20 prices.")
