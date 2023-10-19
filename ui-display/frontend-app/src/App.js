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
          {/* <SuggestedTimeWidget /> */}
        </div>
        <div className="shared-div">
          <div className="left-widget">
            <BusiestWidget />
          </div>
          <div className="right-widget">
            {/* <img
              src={require('../src/flower-icons/bee.png')}
              style={{width: '100px', height: 'auto'}}
            /> */}
            <div className="Joke-box">
              <h3>
                Joke of the day:
              </h3>
              <div>
                <p className="Joke-Question">
                  What's a bee's favourite novel?
                </p>
              </div>
              <div>
                <p className="Joke-Answer">
                  The Great Gats-bee!
                </p>
              </div>
            </div>
          </div>
        </div>
      </div>
      <div className="Grass-box">
        <div className="Names-box">
          <h1>  user_1  </h1>
          <h1>  user_2  </h1>
          <h1>  user_3  </h1>
          <h1>  user_4  </h1>
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

