import React, { useState } from 'react';
import StockGraph from './components/StockGraph';
import StockForm from './components/StockForm';
import StockPrediction from './components/StockPrediction';
import './App.css';

function App() {
  const [prediction, setPrediction] = useState(null);

  const handlePrediction = (data) => {
    setPrediction(data);
  };

  return (
    <div className="App">
      <header className="App-header">
        <h1>Tunisian Stock Market Prediction</h1>
      </header>
      <StockGraph />
      <StockForm onPredict={handlePrediction} />
      {prediction && <StockPrediction prediction={prediction} />}
    </div>
  );
}

export default App;
