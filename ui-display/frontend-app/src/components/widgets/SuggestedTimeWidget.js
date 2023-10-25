import { useState, useEffect } from 'react';
import * as Constants from '../Constants';
import './Widgets.css';

export default function SuggestedTimeWidget() {
    function addSeconds(date, seconds) {
        date.setSeconds(date.getSeconds() + seconds);
        return date;
    }

    const currentToTimeSlotNum = () => {
        const trueNow = new Date();
        const now = addSeconds(trueNow, Constants.TIME_DELTA);
        console.log("now:", now);
        const hour_slot = ((now.getHours() * 60) / Constants.TIMESLOT_LEN) - (5 * 60 / Constants.TIMESLOT_LEN);
        console.log("hour", hour_slot);
        const minute_slot = Math.floor(now.getMinutes() / Constants.TIMESLOT_LEN) * Constants.TIMESLOT_LEN / Constants.TIMESLOT_LEN;
        console.log("minute", minute_slot);
        return hour_slot + minute_slot;
    }

    const dayAndTimeToDate = (day, time) => {
        const timeOptions = {
            hour: "numeric",
            minute: "2-digit",
            hour12: true
        };
        const timeParts = time.split(":");
        const trueNow = new Date();
        const prettyDate = (day.charAt(0).toUpperCase() 
            + day.slice(1)) + " " 
            + (new Date(addSeconds(trueNow, Constants.TIME_DELTA).setHours(timeParts[0], 
                timeParts[1])).toLocaleTimeString('en-AU', timeOptions));
        return prettyDate;
    }

    const [suggestedTime, setSuggestedTime] = useState("");
    const [upcomingEvent, setUpcomingEvent] = useState(null);
    const [loading, setLoading] = useState(true);
    const baseURL = 'https://localhost:8000/display/';


    useEffect(() => {
        const interval = setInterval(()=>{
            fetchData();
            fetchEvents();
        },5000);
        /* DEFAULT BEHAVIOUR: GET SINGLE RECOMMENDATION OF NEXT NEAREST TIME */
        const fetchData = async () => {
            console.log('data fetched');
            const response = await fetch("http://localhost:8000/display/user-free-timeslots");
            const data = await response.json();
            if (data && data.body) {
                const timeSlotsAllWeek = Array.from(data.body);
                // filter out any days already passed
                // TODO what do we do when the week is nearly over?
                const trueNow = new Date();
                const dayName = Constants.DAYS[addSeconds(trueNow, Constants.TIME_DELTA).getDay()];
                console.log(dayName);
                console.log(Constants.DAY_POSITIONS[dayName]);
                console.log("today:", currentToTimeSlotNum());
                    
                const timeSlots = timeSlotsAllWeek.filter(timeSlot => 
                    (Constants.DAY_POSITIONS[timeSlot.day] > Constants.DAY_POSITIONS[dayName]) 
                        || (Constants.DAY_POSITIONS[timeSlot.day] === Constants.DAY_POSITIONS[dayName] 
                            && timeSlot.slot_num > currentToTimeSlotNum()));
                console.log(timeSlots);

                let recommendation = timeSlots[0];
                let recommendations = [];
                let currentSlot = timeSlots[0];
                let numberChecked = 0;
                //console.log("recommendation", recommendations)
                
                let consecutiveSlots = 0;
                while (consecutiveSlots < 3) {
                    //console.log("day", Constants.DAY_POSITIONS[currentSlot.day]);
                    const nextSlot = timeSlots.filter(timeSlot => 
                        (Constants.DAY_POSITIONS[timeSlot.day] === Constants.DAY_POSITIONS[currentSlot.day]) && (timeSlot.slot_num === currentSlot.slot_num + 1)
                    );
                    //console.log("nextSlot", nextSlot);
                    if (nextSlot && nextSlot.length > 0) {
                        console.log("next", nextSlot);
                        //recommendations.push(currentSlot);
                        if (consecutiveSlots == 0) {
                            recommendation = currentSlot;
                        }
                        currentSlot = nextSlot[0];
                        consecutiveSlots++; 
                    } else {
                        consecutiveSlots = 0;
                        if (numberChecked < timeSlots.length) {
                            currentSlot = timeSlots[++numberChecked];
                        } else {
                            console.log("no consecutive times found :(");
                            break;
                        }
                    }
                }

                //console.log(recommendation);

                if (recommendation) {
                    setSuggestedTime(dayAndTimeToDate(recommendation['day'],
                        recommendation['time']));
                    setLoading(false);
                }

            }
        };
        const fetchEvents = async () => {
            const response = await fetch("http://localhost:8000/display/family-timeslots");
            const data = await response.json();
            if (data && data.body) {
                const timeSlotsAllWeek = Array.from(data.body);
                console.log("events:", timeSlotsAllWeek);
                // filter out any days already passed
                // TODO what do we do when the week is nearly over?
                const trueNow = new Date();
                const dayName = Constants.DAYS[addSeconds(trueNow, Constants.TIME_DELTA).getDay()];

                const timeSlots = timeSlotsAllWeek.filter(timeSlot =>
                    (Constants.DAY_POSITIONS[timeSlot.day] > Constants.DAY_POSITIONS[dayName])
                    || (Constants.DAY_POSITIONS[timeSlot.day] === Constants.DAY_POSITIONS[dayName]
                        && timeSlot.slot_num > currentToTimeSlotNum()));
                console.log("events filtered", timeSlots);

                if (timeSlots && timeSlots.length > 0) {
                    console.log("upcoming", timeSlots[0]);
                    setUpcomingEvent(timeSlots[0]);
                } else {
                    console.log("no upcoming events");
                    setUpcomingEvent(null);
                }

            }
        };
        return () => clearInterval(interval);

        //fetchData();
    }, [suggestedTime]); // Empty dependency array means this effect runs once when component mounts


    return (
        <div className="SuggestedTime-box">
            <header>
                {loading ?
                    <p>Oops! Check back in a sec.</p> :
                    <>
                        <h1>Suggested Time 🪩</h1>
                        <h3>Everybody is next free {suggestedTime}.</h3>
                        {upcomingEvent ? 
                            <p> And good news! 🥳 You've got 
                                {(upcomingEvent.data && upcomingEvent.data.length > 1) ? ` ${upcomingEvent.data} ` : " something "}
                                coming up {dayAndTimeToDate(upcomingEvent['day'], upcomingEvent['time'])} 💗
                            </p> 
                        : 
                            <p>Maybe pencil something in!</p>
                        }
                    </>
                }
            </header>
        </div>
    );
}


