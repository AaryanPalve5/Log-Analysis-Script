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
    <div className="min-h-screen bg-gradient-to-r from-blue-500 to-blue-800 text-white">
      <div className="container mx-auto p-8">
        <h1 className="text-4xl font-extrabold text-center mb-12">Log Analysis Dashboard</h1>

        {/* Layout for Desktop: Side by Side */}
        <div className="flex flex-wrap justify-between space-x-6 space-y-8">

          {/* IP Access Count Bar Chart */}
          <div className="w-full lg:w-[48%] p-6 bg-white rounded-lg shadow-xl">
            <h2 className="text-2xl font-semibold text-gray-800 mb-4">IP Access Count</h2>
            <ResponsiveContainer width="100%" height={400}>
              <BarChart data={ipData}>
                <CartesianGrid strokeDasharray="3 3" />
                <XAxis dataKey="ip" />
                <YAxis />
                <Tooltip />
                <Legend />
                <Bar dataKey="count" fill="#6C63FF" barSize={30} />
              </BarChart>
            </ResponsiveContainer>
          </div>

          {/* Most Accessed Endpoint */}
          <div className="w-full lg:w-[48%] p-6 bg-white rounded-lg shadow-xl">
            <h3 className="text-xl font-semibold text-gray-800 mb-4">Most Accessed Endpoint</h3>
            <div className="flex justify-between items-center">
              <div>
                <p className="text-sm text-gray-600">{endpointData.endpoint}</p>
              </div>
              <div className="text-right">
                <p className="text-4xl font-bold text-gray-800">{endpointData.count}</p>
              </div>
            </div>
          </div>

        </div>

        {/* Failed Login Count Table */}
        <div className="p-6 bg-white rounded-lg shadow-xl mt-12">
          <h3 className="text-2xl font-semibold text-gray-800 mb-4">Failed Login Count</h3>
          <table className="min-w-full table-auto">
            <thead>
              <tr>
                <th className="px-6 py-3 text-left font-medium text-gray-600 uppercase">IP Address</th>
                <th className="px-6 py-3 text-left font-medium text-gray-600 uppercase">Failed Login Count</th>
              </tr>
            </thead>
            <tbody>
              {failedLoginData.map((data, index) => (
                <tr key={index} className="border-t hover:bg-gray-100 transition-all duration-200">
                  <td className="px-6 py-3 text-gray-700">{data.ip}</td>
                  <td className="px-6 py-3 text-gray-700">{data.failedCount}</td>
                </tr>
              ))}
            </tbody>
          </table>
        </div>

        {/* Footer with Dashboard Link */}
        
      </div>
    </div>
  );
};

export default Dashboard;
