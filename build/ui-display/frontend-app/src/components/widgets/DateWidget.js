import React from "react";

export default function DateWidget() {
    const prettyDate = (date) => {
        /*
        const timeOptions = {
            hour: "2-digit",
            minute: "2-digit",
            hour12: true
        };*/

        const dateOptions = {
            day: "numeric",
            month: "long",
            year: "numeric"
        };

        return new Date(date).toLocaleString('en-AU', dateOptions); 

        /*
        return [new Date(date).toLocaleTimeString('en-AU', timeOptions), "on",
        new Date(date).toLocaleString('en-AU', dateOptions)].join(" "); */
    }

    return (
        <div className="Date-box">
            <h3>{prettyDate(Date.now())}</h3>
        </div>
    )
}