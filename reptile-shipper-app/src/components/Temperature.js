import React, { useState } from "react";

const TemperatureComponent = ({ maxTemp, minTemp }) => {
  // Define a background color variable based on temperature
  const bgColor =
    maxTemp > 80 ? "bg-red-400" : minTemp < 32 ? "bg-blue-400" : "bg-green-400";

  return (
    <div className={`p-4 rounded-lg text-white ${bgColor} max-w-[80px]`}>
      <p>Max {maxTemp}°F</p>
      <p>Min {minTemp}°F</p>
    </div>
  );
};

export default TemperatureComponent;
