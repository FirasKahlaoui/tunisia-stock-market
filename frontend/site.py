import streamlit as st
import requests

st.title('Tunisian Stock Market Prediction')

# Input fields for the prediction parameters
opening_price = st.number_input('Opening Price')
highest_price = st.number_input('Highest Price')
lowest_price = st.number_input('Lowest Price')
volume = st.number_input('Volume')

# Center the Predict button
st.markdown(""" 
<style>
div.stButton > button:first-child {
    display: block;
    margin: 0 auto;
}
</style>""", unsafe_allow_html=True)

predict_button = st.button('Predict')

if predict_button:
    # Prepare the data for the POST request
    data = {
        'openingPrice': opening_price,
        'highestPrice': highest_price,
        'lowestPrice': lowest_price,
        'volume': volume
    }
    
    try:
        # Send the request to your model's API endpoint
        response = requests.post('http://localhost:5000/predict', json=data)
        
        # Check if the request was successful
        if response.status_code == 200:
            prediction = response.json()
            st.success(f'Predicted Closing Price: {prediction["closingPrice"]}')
        else:
            st.error('Failed to get prediction from the server. Please try again.')
    except requests.exceptions.RequestException as e:
        st.error(f'An error occurred: {e}')

