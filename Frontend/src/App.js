import logo from './logo.svg';
import './App.css';
import Profile from './components/pages/Profile';
import Home from './components/pages/Home';
import { BrowserRouter as Router,Routes, Route, Link } from 'react-router-dom';

function App() {
  return (
    <Router>
      <div className="App">
        <Routes>
            <Route exact path='/' element={<Home />}></Route>
            <Route exact path='/profile' element={<Profile />}></Route>
        </Routes>
      </div>
    </Router>
  );
}

export default App;
