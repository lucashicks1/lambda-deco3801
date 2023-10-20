import './Widgets.css';
import '../../font.css';

import React, { useState, useEffect } from 'react';

export default function ClockWidget() {
  const [currentTime, setCurrentTime] = useState(new Date());

  useEffect(() => {
    // refresh every second
    const interval = setInterval(() => {
      setCurrentTime(new Date());
    }, 1000);

    // Reset the interval on component unmount
    return () => clearInterval(interval);
  }, []);

  return (
    <div>
      <h1>{currentTime.toLocaleTimeString()}</h1>
    </div>
  );
}