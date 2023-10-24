import './Widgets.css';
import '../../font.css';
import {TIME_DELTA} from '../Constants';

import React, { useState, useEffect } from 'react';

export default function ClockWidget() {
  const [currentTime, setCurrentTime] = useState(new Date());

  function addSeconds(date, seconds) {
    date.setSeconds(date.getSeconds() + seconds);
    return date;
  }

  useEffect(() => {
    // refresh every second
    const interval = setInterval(() => {
      const trueNow = new Date();
      setCurrentTime(addSeconds(trueNow, TIME_DELTA));
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