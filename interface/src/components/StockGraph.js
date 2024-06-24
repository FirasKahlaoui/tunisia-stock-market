import React, { useState, useEffect } from 'react';
import { db } from '../firebaseConfig';
import { collection, getDocs } from 'firebase/firestore';
import { LineChart, Line, XAxis, YAxis, CartesianGrid, Tooltip, Legend, ResponsiveContainer } from 'recharts';
import './StockGraph.css';

const StockGraph = () => {
  const [data, setData] = useState([]);

  useEffect(() => {
    const fetchData = async () => {
      const querySnapshot = await getDocs(collection(db, "companies"));
      const stockData = querySnapshot.docs.map(doc => doc.data());
      setData(stockData);
    };

    fetchData();
  }, []);

  return (
    <div className="stock-graph">
      <h2>Stock Price Data</h2>
      <ResponsiveContainer width="100%" height={400}>
        <LineChart data={data} margin={{ top: 5, right: 30, left: 20, bottom: 5 }}>
          <CartesianGrid strokeDasharray="3 3" />
          <XAxis dataKey="date" />
          <YAxis />
          <Tooltip />
          <Legend />
          <Line type="monotone" dataKey="closingPrice" stroke="#8884d8" activeDot={{ r: 8 }} />
        </LineChart>
      </ResponsiveContainer>
    </div>
  );
};

export default StockGraph;
