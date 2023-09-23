import './App.css';
import DateWidget from './components/widgets/DateWidget';
import ClockWidget from './components/widgets/ClockWidget';


function App() {
  return (
    <div className="App">
      <header className="App-header">
        {"hello, world!"}
        <DateWidget />
      </header>
      <ClockWidget />
    </div>
  );
}

export default App;
