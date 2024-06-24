import React, { useState } from 'react';
import axios from 'axios';

function StockForm({ onPredict }) {
  const [formData, setFormData] = useState({
    openingPrice: '',
    highestPrice: '',
    lowestPrice: '',
    volume: '',
  });

  const handleChange = (e) => {
    setFormData({
      ...formData,
      [e.target.name]: e.target.value,
    });
  };

  const handleSubmit = async (e) => {
    e.preventDefault();
    try {
      const response = await axios.post('http://localhost:5000/predict', formData);
      onPredict(response.data);
    } catch (error) {
      console.error('Error predicting stock price:', error);
    }
  };

  return (
    <form onSubmit={handleSubmit}>
      <div>
        <label>Opening Price:</label>
        <input
          type="number"
          name="openingPrice"
          value={formData.openingPrice}
          onChange={handleChange}
        />
      </div>
      <div>
        <label>Highest Price:</label>
        <input
          type="number"
          name="highestPrice"
          value={formData.highestPrice}
          onChange={handleChange}
        />
      </div>
      <div>
        <label>Lowest Price:</label>
        <input
          type="number"
          name="lowestPrice"
          value={formData.lowestPrice}
          onChange={handleChange}
        />
      </div>
      <div>
        <label>Volume:</label>
        <input
          type="number"
          name="volume"
          value={formData.volume}
          onChange={handleChange}
        />
      </div>
      <button type="submit">Predict</button>
    </form>
  );
}

export default StockForm;
