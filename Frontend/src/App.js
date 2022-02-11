import logo from './logo.svg';
import './App.css';
import { useState, useEffect } from 'react';
import Profile from './components/pages/Profile';
import Home from './components/pages/Home';
import { BrowserRouter as Router,Routes, Route, Link } from 'react-router-dom';
import axios from 'axios';

function App() {
  var [profile, setProfile] = useState([])
  useEffect(()=>{
    axios.get("http://127.0.0.1:8000/api/profile/")
      .then(res => {
        profile = res.data;
        setProfile(profile)
      })
      // console.log(profile)
  },[])
  return (
    <Router>
      <div className="App">
        <Routes>
            <Route exact path='/' element={<Home />}></Route>
            <Route exact path='/profile' element={<Profile profile={profile}/>}></Route>
        </Routes>
      </div>
    </Router>
  );
}

export default App;
