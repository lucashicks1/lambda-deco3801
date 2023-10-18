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
            <h2 className="SuggestedActivity-box">it's looking {weatherCondition.toLowerCase()} today, how about a {activity}?</h2>
    );
}

export default Activities;