import './App.css';
import DateWidget from './components/widgets/DateWidget';
import ClockWidget from './components/widgets/ClockWidget';
import WeatherWidget from './components/widgets/WeatherWidget';
import SuggestedActivityWidget from './components/widgets/SuggestedActivityWidget';
import BusiestWidget from './components/widgets/BusiestWidget';
import SuggestedTimeWidget from './components/widgets/SuggestedTimeWidget';

function App() {
  return (
    // <div className="App">
    //   <header className="App-header">
    //     <div className="Clock-box">
    //     <ClockWidget />
    //     </div>
    //     <DateWidget />
    //   </header>
    //   <div className="Sky-box">
    //     <BusiestWidget />
    //     <SuggestedTimeWidget />
    //     here's the sky
    //   </div>
    //   <div className='Grass-box'>
    //       here's the grass :D
    //   </div>
    // </div>
    <div className="App">
      <div className="Sky-box">
        <div>
          <div className="Clock-box">
            <ClockWidget />
            <div className="Date-box">
              <DateWidget />
            </div>
          </div>
        </div>
        <div className="shared-div">
          <div className="left-widget">
            <WeatherWidget />
          </div>
          <div className="right-widget">
            <SuggestedActivityWidget />
          </div>
        </div>
        <div className="SuggestedTime-box">
          {/* <SuggestedTimeWidget /> */}
        </div>
      </div>
      <div className="Grass-box">
        {/* grass here */}
      </div>
    </div>
  );
}

export default App;

