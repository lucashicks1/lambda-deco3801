import { useState, useEffect } from 'react';
import * as Constants from '../Constants';
import './Widgets.css';

export default function SuggestedTimeWidget() {

    const currentToTimeSlotNum = () => {
        const now = new Date();
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
        const prettyDate = (day.charAt(0).toUpperCase() 
            + day.slice(1)) + " " 
            + (new Date(new Date().setHours(timeParts[0], 
                timeParts[1])).toLocaleTimeString('en-AU', timeOptions));
        return prettyDate;
    }

    const [suggestedTime, setSuggestedTime] = useState("");
    const [loading, setLoading] = useState(true);
    const baseURL = 'https://localhost:8000/display/';


    useEffect(() => {
        const interval = setInterval(()=>{
            fetchData();
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
                const dayName = Constants.DAYS[new Date().getDay()];
                console.log(dayName);
                console.log(Constants.DAY_POSITIONS[dayName]);
                console.log("today:", currentToTimeSlotNum());
                    
                const timeSlots = timeSlotsAllWeek.filter(timeSlot => 
                    (Constants.DAY_POSITIONS[timeSlot.day] > Constants.DAY_POSITIONS[dayName]) 
                        || (Constants.DAY_POSITIONS[timeSlot.day] === Constants.DAY_POSITIONS[dayName] 
                            && timeSlot.slot_num > currentToTimeSlotNum()));
                setSuggestedTime(dayAndTimeToDate(timeSlots[0]['day'],
                    timeSlots[0]['time']));
                setLoading(false);
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
                    </>
                }
            </header>
        </div>
    );
}


