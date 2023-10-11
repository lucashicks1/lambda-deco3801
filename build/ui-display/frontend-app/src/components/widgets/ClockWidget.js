import './Widgets.css';
import React, { useState, useEffect } from 'react';

export default function ClockWidget() {
  const [currentTime, setCurrentTime] = useState(new Date());

  useEffect(() => {
    const interval = setInterval(() => {
      setCurrentTime(new Date());
    }, 1000);

    // Clean up the interval on component unmount
    return () => clearInterval(interval);
  }, []);

  return (
    <div>
      <h1>{currentTime.toLocaleTimeString()}</h1>
    </div>
  );
}