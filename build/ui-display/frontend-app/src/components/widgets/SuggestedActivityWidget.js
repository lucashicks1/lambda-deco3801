import React from 'react';

const weatherActivities = {
    'Thunderstorm': 'movie marathon',
    'Drizzle': 'bake off',
    'Rain': 'trip to the library',
    'Clear': 'picnic',
    'Clouds': 'game of Catan'
};

const weatherConditionText = {
    'Thunderstorm': 'like there\'s a storm coming',
    'Drizzle': 'dreary',
    'Rain': 'rainy',
    'Clear': 'beautifully clear',
    'Clouds': 'cloudy'
};


const Activities = ({ currentCondition }) => {
    // hard code this value for now
    if (!currentCondition) {
        currentCondition = 'Clouds';
    }
    // Get the corresponding activity based on the weatherCondition
    const activity = weatherActivities[currentCondition] || 'movie';
    const text = weatherConditionText[currentCondition] || 'clear';

    return (
            <h2 className="SuggestedActivity-box">it's looking {text} today, how about a {activity}?</h2>
    );
}

export default Activities;