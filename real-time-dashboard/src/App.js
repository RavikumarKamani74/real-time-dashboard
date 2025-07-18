import React, { useEffect, useState } from "react";
import "./App.css";

function App() {
  const [metrics, setMetrics] = useState([]);

  useEffect(() => {
    fetch("https://xexy5jnghe.execute-api.ap-south-2.amazonaws.com/dev/metrics?metric_id=cpu")
      .then((response) => response.json())
      .then((data) => {
        console.log("Fetched data:", data);
        setMetrics(data);
      })
      .catch((error) => {
        console.error("Error fetching metrics:", error);
      });
  }, []);

  return (
    <div className="App" style={{ padding: "20px", fontFamily: "Arial" }}>
      <h1>📊 CPU Metrics Dashboard</h1>
      <table border="1" cellPadding="10">
        <thead>
          <tr>
            <th>Timestamp</th>
            <th>Value</th>
          </tr>
        </thead>
        <tbody>
          {metrics.map((metric, index) => (
            <tr key={index}>
              <td>{new Date(metric.timestamp * 1000).toLocaleString()}</td>
              <td>{metric.value}</td>
            </tr>
          ))}
        </tbody>
      </table>
    </div>
  );
}

export default App;
