import { useState, useEffect } from 'react';
import * as Constants from '../Constants';
import './Widgets.css';

export default function SuggestedTimeWidget() {
    
    /* SETTINGS FOR CONFIG:
    - how many times to suggest if there's more than 1 appropriate?
    - what to display if there are none appropriate?
        - SWITCH to next best times instead?
        - or explicitly say there's no good times and direct to DIFFERENT widget?
    - when there's multiple matches, what do we rank by?
        - next nearest time?

    - if the week is nearly over, do you treat entries like they wrap to the next
    week coming (e.g. on a friday, stuff written on monday becomes NEXT monday),
    or just cut the week off after the remaining fri, sat, sun?

    - day the week starts? (remember to update Constants file accordingly.
        if this is going to change dynamically maybe move that dictionary 
        to a Utilities file instead).

    - should we report how long eveyrbody is free for, i.e. does it span multiple
    time slots? or should they just be able to set the minimum number of consecutive
    time slots required for it to "count"?
    */
    const currentToTimeSlotNum = () => {
        const now = new Date();
        const hour_slot = now.getHours() * 60 / Constants.TIMESLOT_LEN;
        const minute_slot = Math.floor(now.getMinutes() / Constants.TIMESLOT_LEN) * Constants.TIMESLOT_LEN / Constants.TIMESLOT_LEN;
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
            fetchData()
        },200000)
        /* DEFAULT BEHAVIOUR: GET SINGLE RECOMMENDATION OF NEXT NEAREST TIME */
        const fetchData = async () => {
            const response = await fetch("http://localhost:8000/display/user-free-timeslots");
            const data = await response.json();
            if (data && data.body) {
                const timeSlotsAllWeek = Array.from(data.body);
                // filter out any days already passed
                // TODO what do we do when the week is nearly over?
                const dayName = Constants.DAYS[new Date().getDay()];
                const timeSlots = timeSlotsAllWeek.filter(timeSlot => 
                    (Constants.DAY_POSITIONS[timeSlot.day] 
                        > Constants.DAY_POSITIONS[dayName]) 
                        || (Constants.DAY_POSITIONS[timeSlot.day] 
                            === Constants.DAY_POSITIONS[dayName] 
                            && timeSlot.slot_num > currentToTimeSlotNum()));
                setSuggestedTime(dayAndTimeToDate(timeSlots[0]['day'],
                    timeSlots[0]['time']));
                setLoading(false);
            }
        };

        fetchData();
    }, []); // Empty dependency array means this effect runs once when component mounts


    return (
        <div className="SuggestedTime-box">
            <header>
                {loading ?
                    <p>Oops! Check back in a sec.</p> :
                    <>
                        <h1>Suggested Time 🪩</h1>
                        <h3>Everybody is next free at {suggestedTime}.</h3>
                    </>
                }
            </header>
        </div>
    );
}


