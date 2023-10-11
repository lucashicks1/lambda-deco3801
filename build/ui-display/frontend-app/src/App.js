import './App.css';
import DateWidget from './components/widgets/DateWidget';
import ClockWidget from './components/widgets/ClockWidget';
import BusiestWidget from './components/widgets/BusiestWidget';
import SuggestedTimeWidget from './components/widgets/SuggestedTimeWidget';

function App() {
  return (
    <div className="App">
      <header className="App-header">
        {"hello, world!"}
        <DateWidget />
      </header>
      <ClockWidget />
      <div className="Sky-box">
        <BusiestWidget />
        <SuggestedTimeWidget />
        here's the sky
        <div className='Grass-box'>
          here's the grass :D
        </div>
      </div>
    </div>
  );
}

export default App;

