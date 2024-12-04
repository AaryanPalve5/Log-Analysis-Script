import React from 'react';
import { BarChart, Bar, XAxis, YAxis, CartesianGrid, Tooltip, Legend, ResponsiveContainer } from 'recharts';

const Dashboard = () => {
  // Sample Data for IP Access Count
  const ipData = [
    { ip: '203.0.113.5', count: 8 },
    { ip: '198.51.100.23', count: 8 },
    { ip: '192.168.1.1', count: 7 },
    { ip: '10.0.0.2', count: 6 },
    { ip: '192.168.1.100', count: 5 },
  ];

  // Data for Most Accessed Endpoint
  const endpointData = {
    endpoint: '/login',
    count: 13,
  };

  // Data for Failed Login Count
  const failedLoginData = [
    { ip: '203.0.113.5', failedCount: 8 },
    { ip: '192.168.1.100', failedCount: 5 },
  ];

  return (
    <div className="container mx-auto p-4">
      <h1 className="text-3xl font-semibold mb-6 text-center">Log Analysis Dashboard</h1>

      {/* Bar Chart Section */}
      <div className="p-4 bg-white shadow-lg rounded-lg mb-8">
        <h2 className="text-xl font-bold mb-4">IP Access Count</h2>
        <ResponsiveContainer width="100%" height={400}>
          <BarChart data={ipData}>
            <CartesianGrid strokeDasharray="3 3" />
            <XAxis dataKey="ip" />
            <YAxis />
            <Tooltip />
            <Legend />
            <Bar dataKey="count" fill="#4c51bf" />
          </BarChart>
        </ResponsiveContainer>
      </div>

      {/* Most Accessed Endpoint Section */}
      <div className="p-4 bg-white shadow-lg rounded-lg mb-8 flex items-center justify-between">
        <div>
          <h3 className="text-lg font-semibold">Most Accessed Endpoint</h3>
          <p className="text-sm text-gray-600">{endpointData.endpoint}</p>
        </div>
        <div className="text-right">
          <p className="text-4xl font-bold">{endpointData.count}</p>
        </div>
      </div>

      {/* Failed Login Count Section */}
      <div className="p-4 bg-white shadow-lg rounded-lg mb-8">
        <h3 className="text-xl font-semibold mb-4">Failed Login Count</h3>
        <table className="min-w-full table-auto">
          <thead>
            <tr>
              <th className="px-4 py-2 text-left font-semibold text-gray-600">IP Address</th>
              <th className="px-4 py-2 text-left font-semibold text-gray-600">Failed Login Count</th>
            </tr>
          </thead>
          <tbody>
            {failedLoginData.map((data, index) => (
              <tr key={index} className="border-t">
                <td className="px-4 py-2 text-gray-700">{data.ip}</td>
                <td className="px-4 py-2 text-gray-700">{data.failedCount}</td>
              </tr>
            ))}
          </tbody>
        </table>
      </div>

    </div>
  );
};

export default Dashboard;
