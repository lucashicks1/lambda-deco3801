import './App.css';
import DateWidget from './components/widgets/DateWidget';
import ClockWidget from './components/widgets/ClockWidget';
import WeatherWidget from './components/widgets/WeatherWidget';
import SuggestedActivityWidget from './components/widgets/SuggestedActivityWidget';
import './font.css';
import BusiestWidget from './components/widgets/BusiestWidget';
import SuggestedTimeWidget from './components/widgets/SuggestedTimeWidget';

function App() {

  return (
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
          <SuggestedTimeWidget />
        </div>
        <div className="shared-div">
          <div className="left-widget">
            <BusiestWidget />
          </div>
        </div>
      </div>
      <div className="Grass-box">
      
      </div>
    </div>
  );
}

export default App;

