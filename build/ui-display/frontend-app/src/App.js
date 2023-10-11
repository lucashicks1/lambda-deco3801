import './App.css';
import DateWidget from './components/widgets/DateWidget';
import ClockWidget from './components/widgets/ClockWidget';
import WeatherWidget from './components/widgets/WeatherWidget';


function App() {
  return (
    <div className="App">
      <header className="App-header">
        <ClockWidget />
        <DateWidget />
      </header>
    </div>
  );
}

export default App;
