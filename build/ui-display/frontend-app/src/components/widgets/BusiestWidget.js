import {useState, useEffect} from 'react';
import './Widgets.css';

export default function BusiestWidget() {
    const [busiest, setBusiest] = useState("");
    const [loading, setLoading] = useState(true);

    const baseURL = 'https://localhost:8000/display/';

    useEffect(() => {
        const fetchData = async () => {
            const response = await fetch("http://localhost:8000/display/user-totals");
            const data = await response.json();
            if (data) {
                const times = Object.values(data);
                setBusiest(Object.entries(data).filter(([key, value]) => value === Math.max(...times)).map(([key, value]) => key));
                setLoading(false);
                
            } 
        };

        fetchData();
    }, []); // Empty dependency array means this effect runs once when component mounts

    
    return (
        <div className="BusiestWidget">
            <header>
                {loading ? 
                    <p>Oops! Check back in a sec.</p> : 
                    <>
                        <h1>Busy Bee 🐝</h1>
                        <h3>The busiest bee in the house this week is {busiest}. Wish them luck!</h3>
                    </>
                }
            </header>
        </div>
    );
}


