import React from 'react';
import profileimg from '../img/profile.jpg';
import '../css/base.css';
import '../css/profile.css';
import { IoLogoFacebook } from "react-icons/io5";
import { IoLogoWhatsapp } from "react-icons/io5";
import { IoPencilSharp } from "react-icons/io5";
import { IoAdd } from "react-icons/io5";
import dummy1 from '../img/dummy1.jpg';
import dummy2 from '../img/dummy2.jpg';
import dummy3 from '../img/dummy3.jpg';
import axios from 'axios';
import { useState, useEffect } from 'react';


const Profile = ({profile1}) => {
    var [profile, setProfile] = useState({
        first_name: '',
        last_name: '',
        sso_id: '',
    })
    useEffect(()=>{
        axios.get("http://127.0.0.1:8000/api/profile/?user_id=200010050")
        // .then((res) => res.json())
          .then((result) => {
              console.log(result)
            setProfile(result.data)
          })
          console.log("Profile is" )
          console.log(profile)
        //   console.log(res.data)
      },[])
    // axios.get("http://127.0.0.1:8000/api/profile/"+{profile}, person)
    //         .then(function(res){
    //             console.log(res)
    //         })
    const user_id = localStorage.getItem('profile')
    const [person, setPerson] = useState({
        name : '',
        rollno: ''
    })
    const inputsHandler = (e) =>{
        setPerson( {...person, [e.target.name]: e.target.value} )
    }
    
    const handleSubmit = async (e) => {
        e.preventDefault();
        
    }
     
    return (
/*         <div class = "row">
            <div className="col-md-5">
                hello
            </div>
        </div> */
        
        
        <div>
            <div className="background">
        <div className="shape"></div>
        <div className="shape"></div>
        <div className="shape"></div>
    </div>
            <div className='dp-section'>
               
                <div className='dp blur-back'>
                    <h2>{profile.sso_id}</h2>
                    <img src={profileimg}></img>
                    <h2>Tagline</h2>
                </div>
                <div className='dp-desc blur-back'>
                <div className='edit-profile'><IoPencilSharp></IoPencilSharp></div>
                    <h2>Name: {profile.first_name}</h2>
                    <h3>Description</h3>
                    <h3>In My insti life, never have I ever:</h3>
                    <div className='share-social'>
                        <li style={{marginLeft: "0px", paddingLeft: "0px"}}><IoLogoFacebook></IoLogoFacebook></li>
                        <li><IoLogoWhatsapp></IoLogoWhatsapp></li>
                    </div>
                </div>
            </div>
            <div className='image-gallery blur-back'>
                <div className='add-image'><IoAdd></IoAdd></div>
                <h1>Image Gallery</h1>
                <div className='gallery row '>
{/*                     <div className='big-image'>
                        <img src={dummy1}></img>
                    </div> */}
                    
                        <div className="col">
                            <img src={dummy1} className = "img-fluid"></img>
                        </div>
                        <div className="col">
                            <img src={dummy1} className = "img-fluid"></img>
                        </div>
                        <div className="col">
                            <img src={dummy1} className = "img-fluid"></img>
                        </div>
                        <div className="col">
                            <img src={dummy1} className = "img-fluid"></img>
                        </div>
                    
                </div>
            </div>
            <form onSubmit={handleSubmit}>
                <input placeholder='Name' onChange={inputsHandler} value={person.name} name='name'></input>
                <input placeholder='roll' onChange={inputsHandler} value={person.rollno} name='rollno'></input>
                <button type='submit'>Submit</button>
            </form>
        </div>
    )
}

export default Profile
