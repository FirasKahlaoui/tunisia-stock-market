import React from 'react';

function StockPrediction({ prediction }) {
  return (
    <div>
      <h2>Stock Price Prediction</h2>
      <p>Predicted Closing Price: {prediction.closingPrice}</p>
      <p>Additional Info: {prediction.additionalInfo}</p>
    </div>
  );
}

export default StockPrediction;
