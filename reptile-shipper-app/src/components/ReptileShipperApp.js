import React, { useState } from "react";

const ReptileShipperApp = () => {
  const [city, setCity] = useState("");
  const [state, setState] = useState("");
  const [weatherData, setWeatherData] = useState(null);
  const [loading, setLoading] = useState(false);
  const [error, setError] = useState("");

  const handleCityChange = (event) => setCity(event.target.value);
  const handleStateChange = (event) => setState(event.target.value);

  const handleSubmit = async () => {
    if (!city || !state) {
      alert("Please enter both city and state");
      return;
    }
    let baseUrl = 'invalid';
    console.log('baseurl:',baseUrl);
    // Running locally with npm start
    if (process.env.NODE_ENV === 'development') {
      baseUrl = process.env.REACT_APP_LOCAL_API_BASE_URL;
    }
    // Running npm run build in prod
    if (process.env.NODE_ENV === 'production'){
      baseUrl = process.env.REACT_APP_PRODUCTION_API_BASE_URL;
    }

    const apiUrl = `${baseUrl}/weather/${state}/${city}`;
    const headers = {
      "Content-Type": "application/json",
      "x-api-key": `${process.env.REACT_APP_REPTILE_SHIPPER_API_KEY}`,
    };
    console.log("api url:",apiUrl);
    try {
      const response = await fetch(apiUrl, {
        method: "GET",
        headers: headers,
      });
      if (!response.ok) {
        throw new Error("Failed to fetch weather data");
      }
      const data = await response.json();
      setWeatherData(data); // Set the data to state
    } catch (error) {
      setError(error.message); // Handle any errors
    } finally {
      setLoading(false);
    }
  };

  return (
    <div className="flex flex-col justify-center items-center min-h-screen bg-gray-100">
      <div className="p-2 bg-white shadow-md rounded-lg w-half max-w-md text-center">
      <h1 className="text-l font-bold text-gray-800 mb-2">Weather App</h1>
      </div>
      <input
        type="text"
        placeholder="Enter full city name"
        value={city}
        onChange={handleCityChange}
        className="border p-2 my-2 rounded"
      />
      <input
        type="text"
        placeholder="Enter state (e.g. CA)"
        value={state}
        onChange={handleStateChange}
        className="border p-2 my-2 rounded"
      />
      <button className = "border border-gray-500 px-4 py-2 rounded"><button onClick={handleSubmit}>Get Weather</button></button>

      {weatherData && (
        <div className="p-4 max-w-md mx-auto bg-white rounded-lg shadow-md">
          <h1 className="text-xl font-bold text-gray-800">
            Weather in {weatherData.city}, {weatherData.state}
          </h1>
          <ul className="mt-4">
            {weatherData.temps.daily_temps.map((day) => (
              <li key={day.date} className="flex justify-between p-2 border-b">
                <span className="text-gray-700">{day.date}</span>
                <span className="text-blue-600">
                  Max: {day.temps.max_temp}°C
                </span>
                <span className="text-red-600">
                  Min: {day.temps.min_temp}°C
                </span>
              </li>
            ))}
          </ul>
        </div>
      )}
    </div>
  );
};

export default ReptileShipperApp;
