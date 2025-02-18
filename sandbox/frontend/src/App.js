import React, { useState } from "react";
import { BarChart, Bar, XAxis, YAxis, Tooltip, ResponsiveContainer } from "recharts";

function App() {
  const [ip, setIp] = useState("");
  const [result, setResult] = useState(null);
  const [error, setError] = useState("");

  const checkIP = async () => {
    setError("");
    setResult(null);

    if (!ip) {
      setError("Please enter an IP address.");
      return;
    }

    try {
      const response = await fetch("http://127.0.0.1:5000/api/check_ip", {
        method: "POST",
        headers: { "Content-Type": "application/json" },
        body: JSON.stringify({ ip }),
      });

      const data = await response.json();
      setResult(data);
    } catch (err) {
      setError("Error fetching data. Check backend connection.");
    }
  };

  return (
    <div>
      <h1>Cyber Threat Intelligence Dashboard</h1>
      <input
        type="text"
        placeholder="Enter an IP address..."
        value={ip}
        onChange={(e) => setIp(e.target.value)}
      />
      <button onClick={checkIP}>Check IP</button>

      {error && <p style={{ color: "red" }}>{error}</p>}

      {result && (
        <div>
          <h2>IP Report:</h2>
          <p><strong>IP:</strong> {result.data?.ipAddress}</p>
          <p><strong>Abuse Score:</strong> {result.data?.abuseConfidenceScore}</p>
          <p><strong>ISP:</strong> {result.data?.isp}</p>
          <p><strong>Country:</strong> {result.data?.countryCode}</p>

          <h3>Threat Visualization</h3>
          <ResponsiveContainer width="100%" height={300}>
            <BarChart data={[{ name: "Abuse Score", value: result.data?.abuseConfidenceScore }]}>
              <XAxis dataKey="name" />
              <YAxis />
              <Tooltip />
              <Bar dataKey="value" fill="red" />
            </BarChart>
          </ResponsiveContainer>
        </div>
      )}
    </div>
  );
}

export default App;
