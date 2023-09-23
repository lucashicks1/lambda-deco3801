import './App.css';
import './components/widgets/ClockWidget'
import ClockWidget from './components/widgets/ClockWidget';

function App() {
  return (
    <div className="App">
      <header className="App-header">
        {"hello, world!"}
      </header>
      <ClockWidget />
    </div>
  );
}

export default App;
