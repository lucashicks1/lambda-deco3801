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
          <div className="right-widget">
            <div className="Joke-box">
              <h2>
                Joke of the day:
              </h2>
              <div>
                <h2 className="Joke-Question">
                  What's a bee's favourite novel?
                </h2>
              </div>
              <div>
                <h2 className="Joke-Answer">
                  The Great Gats-bee!
                </h2>
              </div>
            </div>
          </div>
        </div>
      </div>
      <div className="Grass-box">
        <div className="Names-box">
          <h1>  Timmy  </h1>
          <h1>  Jimmy  </h1>
          <h1>  Kimmy  </h1>
          <h1>  Timmy Jr  </h1>
        </div>
        <div className="Names-box">
          <img src={require('../src/flower-icons/3flower.png')} />
          <img src={require('../src/flower-icons/15flower.png')} />
          <img src={require('../src/flower-icons/18flower.png')} />
          <img src={require('../src/flower-icons/30flower.png')} />
        </div>
      </div>
    </div>
  );
}

export default App;

