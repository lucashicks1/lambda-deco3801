import React from "react";
import { TIME_DELTA } from '../Constants';

export default function DateWidget() {
    function addSeconds(date, seconds) {
        date.setSeconds(date.getSeconds() + seconds);
        return date;
    }
    const prettyDate = (date) => {

        const dateOptions = {
            day: "numeric",
            month: "long",
            year: "numeric"
        };

        return new Date(date).toLocaleString('en-AU', dateOptions); 
    }

    const trueNow = new Date();

    return (
        <div className="Date-box">
            <h3>{prettyDate(addSeconds(trueNow, TIME_DELTA))}</h3>
        </div>
    )
}