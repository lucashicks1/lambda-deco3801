import React, { Component } from "react";
import axios from 'axios';

class WeatherWidget extends Component {
    state = {
        temperature: null,
        icon: null,
        condition: null
    };

    componentDidMount() {
        this.fetchWeatherCondition();
        this.refreshInterval = setInterval(this.fetchWeatherCondition, 3600000);
    }

    componentWillUnmount() {
        clearInterval(this.refreshInterval);
    }

    fetchWeatherCondition = () => {
        const apiKey = 'e032a9d4b172cf16a8f75efac7a4470c';
        const stLuciaLat = 27.5021;
        const stLuciaLon = 152.9968;
        const apiUrl = `https://api.openweathermap.org/data/2.5/weather?lat=${stLuciaLat}&lon=${stLuciaLon}&appid=${apiKey}&units=metric`;
    
        axios.get(apiUrl).then((response) => {
            const { main, weather } = response.data;
            const temperature = main.temp;
            const icon = weather[0].icon;
            const condition = weather[0].main;
            this.setState({ temperature, icon, condition });
        }).catch((error) => {
            console.error('Error fetching weather data:', error);
        });
    };

    render() {
        const { temperature, icon } = this.state;

        return (
            <div>
                {temperature !== null && (
                    <div>
                        <h2>{temperature}°C</h2>
                        {icon && (
                            <img
                                src={`https://openweathermap.org/img/w/${icon}.png`}
                                alt="Weather Icon"
                            />
                        )}
                    </div>
                )}
            </div>
        );
    }
}

export default WeatherWidget;