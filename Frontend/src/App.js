import logo from './logo.svg';
import 'bootstrap/dist/css/bootstrap.min.css';  
import './App.css';
import { useState, useEffect } from 'react';
import Profile from './components/pages/Profile';
import Home from './components/pages/Home';
import Login from './components/pages/Login';
import Navbar_func from './components/Navbar';
import { BrowserRouter as Router,Routes, Route, Link } from 'react-router-dom';
import axios from 'axios';
import { Navbar, Container, Nav } from 'react-bootstrap';


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
  const setstudentData = (student) => {
      setProfile(student)
      localStorage.setItem('profile', student)
  }
  useEffect(()=>{
    setProfile(localStorage.getItem('profile'))
  })
  return (
    <Router>
      <div className="App">
        <Navbar_func/>
        <Routes>
            <Route exact path='/' element={<Login setstudentData={setstudentData}/>}></Route>
            <Route exact path='/profile' element={<Profile profile={profile}/>}></Route>
        </Routes>
      </div>
    </Router>
  );
}

export default App;
