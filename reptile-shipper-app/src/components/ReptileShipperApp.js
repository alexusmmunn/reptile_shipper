import React, { useState } from "react";

const capitalizeFirstLetter = (value) => {
  if (!value) return "";
  return value.charAt(0).toUpperCase() + value.slice(1).toLowerCase();
};

const WeatherForecast = () => {
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
    if (process.env.NODE_ENV === 'development') {
      baseUrl = process.env.REACT_APP_LOCAL_API_BASE_URL;
    }
    if (process.env.NODE_ENV === 'production'){
      baseUrl = process.env.REACT_APP_PRODUCTION_API_BASE_URL;
    }

    const apiUrl = `${baseUrl}/weather/${state}/${city}`;
    const headers = {
      "Content-Type": "application/json",
      "x-api-key": `${process.env.REACT_APP_REPTILE_SHIPPER_API_KEY}`,
    };
    try {
      setLoading(true);
      const response = await fetch(apiUrl, { method: "GET", headers: headers });
      if (!response.ok) {
        throw new Error("Failed to fetch weather data");
      }
      const data = await response.json();
      setWeatherData(data);
    } catch (error) {
      setError(error.message);
    } finally {
      setLoading(false);
    }
  };

  return (
    <div className="flex flex-col justify-center items-center min-h-screen bg-gray-100">
      <div className="p-2 bg-white shadow-md rounded-lg w-half max-w-md text-center">
        <h1 className="text-l font-bold text-gray-800 mb-2">Reptile Shipper</h1>
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
      <button className="border border-gray-500 px-4 py-2 rounded" onClick={handleSubmit}>Get Weather</button>
      {loading && <p>Loading...</p>}
      {error && <p>Error: {error}</p>}
      {weatherData && (
        <div className="p-4 max-w-md mx-auto bg-white rounded-lg shadow-md">
          <h1 className="text-xl font-bold text-gray-800">
            Weather in {capitalizeFirstLetter(weatherData.city)}, {weatherData.state.toUpperCase()}
          </h1>
          <div className="flex overflow-x-auto space-x-4 p-2 border border-gray-300">
            {Object.entries(weatherData.temps).map(([date, temps]) => (
              <li key={date} className="flex flex-col items-center p-2 border rounded bg-gray-50">
                <span className="text-gray-700 font-semibold">{date} </span>
                <span className="text-blue-600"> Max: {temps[1]}°F</span>
                <span className="text-red-600"> Min: {temps[0]}°F</span>
              </li>
            ))}
          </div>
        </div>
      )}
    </div>
  );
};

export default WeatherForecast;
