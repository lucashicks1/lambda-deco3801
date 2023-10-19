import React from "react";

export default function DateWidget() {
    const prettyDate = (date) => {

        const dateOptions = {
            day: "numeric",
            month: "long",
            year: "numeric"
        };

        return new Date(date).toLocaleString('en-AU', dateOptions); 
    }

    return (
        <div className="Date-box">
            <h3>{prettyDate(Date.now())}</h3>
        </div>
    )
}