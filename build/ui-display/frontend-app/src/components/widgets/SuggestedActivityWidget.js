// import React from "react";

// export default function ClockWidget() { 
//     const Activities = ({ weatherCondition }) => {

//         const weatherActivities = {
//             'Thunderstorm': 'movie marathon',
//             'Drizzle': 'bake off',
//             'Rain': 'trip to the library',
//             'Clear': 'picnic',
//             'Clouds': 'game of Catan'
//         };
        
//         const weather = 'Clear';
//         const activity = weatherActivities[weather] || 'movie';
//     }


    
//         return (
//             <div>
//                 <h1>It's looking {weatherCondition} today, how about a {activity}?</h1>
//             </div>
//         );
// }

import React from 'react';

const weatherActivities = {
    'Thunderstorm': 'movie marathon',
    'Drizzle': 'bake off',
    'Rain': 'trip to the library',
    'Clear': 'picnic',
    'Clouds': 'game of Catan'
};

const Activities = ({ weatherCondition }) => {
    // hard code this value for now
    if (!weatherCondition) {
        weatherCondition = 'Clear';
    }
// Get the corresponding activity based on the weatherCondition
    const activity = weatherActivities[weatherCondition] || 'movie';

    return (
        <div>
            <h1>It's looking {weatherCondition} today, how about a {activity}?</h1>
        </div>
    );
}

export default Activities;