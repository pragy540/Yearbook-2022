import React, { useState } from "react";
import Form from "react-bootstrap/Form";
import Button from "react-bootstrap/Button";
import "../css/Login.css";
import "../css/base.css";
import axios from 'axios';
import { Navigate } from 'react-router-dom';

function getCookie(name) {
    var cookieValue = null;
    if (document.cookie && document.cookie !== '') {
        var cookies = document.cookie.split(';');
        for (var i = 0; i < cookies.length; i++) {
            var cookie = cookies[i].trim();
            // Does this cookie string begin with the name we want?
            if (cookie.substring(0, name.length + 1) === (name + '=')) {
                cookieValue = decodeURIComponent(cookie.substring(name.length + 1));
                break;
            }
        }
    }
    return cookieValue;
}
var csrftoken = getCookie('csrftoken');

export default function Login({setstudentData}) {
const [student, setStudent] = useState(
    {
        first_name: '',
        last_name: '',
        email: '',
        iitb_org: '',
        otp_field: ''
    }
)
const [redirect, setRed] = useState(false)

function validateForm() {
    return student.email.length > 0
}




function handleChange(e) {
    setStudent( {...student, [e.target.name]: e.target.value} )
}
function handleSubmit(event) {
    console.log(student)
    event.preventDefault();
    axios.post("http://127.0.0.1:8000/api/register/", student, { headers: { 'X-CSRFToken': csrftoken }})
            .then(function(res){
                console.log(res)
                
                setRed(!redirect)
            })
            .catch((error)=>{
                console.log(error)
            })
        }
    
    // fetch("http://127.0.0.1:8000/api/register", {
    //     method: "POST",
    //     headers: {
    //         "Content-Type" : "application/json"
    //     },
    //     body: JSON.stringify(student)
    // }).then((res) => res.json())
    // .then((result) => console.log(result))
    // .catch((err) => console.log(err))
    // }
    if (redirect) {
        return <Navigate to="/profile"></Navigate>
    }
return (
    <div className="Login">
        
        <div className="body">
    <Form onSubmit={handleSubmit}>
    <div className="head">Welcome To The YearBook!
        <br />
        </div>
        <div className="head2">
        Fill the form below to login
        </div>
        <Form.Group size="lg" controlId="firstname">
        <Form.Label>First name:</Form.Label>
        <br />
        <Form.Control type="text" size="lg" name="first_name" value={student.first_name} onChange={handleChange}
        placeholder="First name" />
        </Form.Group>
        <div className="description">Enter your first name</div>
        <Form.Group size="lg" controlId="lastname">
        <Form.Label>Last name:</Form.Label>
        <br />
        <Form.Control type="text" 
        placeholder="Last name " name="last_name" value={student.last_name} onChange={handleChange} />
        </Form.Group>
        <div className="description">Enter your last name</div>
        <Form.Group size="lg" controlId="email">
        <Form.Label>Roll Number </Form.Label>
        <br />
        <Form.Control
            autoFocus
            type="text"
            placeholder="200020057"
            value={student.email}
            name="email"
            onChange={handleChange}
        />
        </Form.Group>
        <div className="description">Enter your roll number: Email will be sent to roll-no@iitb.ac.in</div>
        <Form.Group size="lg" controlId="password">
        <Form.Label>Username (iitbombay.org)</Form.Label>
        <br/>
        <Form.Control
            type="text"
            name="iitb_org"
            value={student.iitb_org}
            onChange={handleChange}
        />
        <div className="description">Enter your iitbombay.org username: Email will be sent to username@iitbombay.org.
        Use only if you're an alumni, and don't have email forwarding enabled 
        </div>
        </Form.Group>
        <Form.Group size="lg" controlId="email">
        <Form.Label>Otp field </Form.Label>
        <br />
        <Form.Control
            autoFocus
            type="text"
            placeholder="Eg 123456 or leave blank to generate an otp"
            value={student.otp_field}
            name="otp_field"
            onChange={handleChange}
        />
        </Form.Group>
        <div className="description">Enter the 6 digit OTP you recieved on your email (roll-no@iitb.ac.in). Leave blank to Generate a new OTP</div>
        <div className="btn">
        {student.otp_field == '' ? 
        <Button block size="lg" type="submit" disabled={!validateForm()}>
        Generate OTP
        </Button>   
        :
        <Button block size="lg" type="submit" disabled={!validateForm()} onClick={() => setstudentData(student.email)}>
        Submit
        </Button>
}
        </div>
        <br/>

    </Form>
    <br/>
    </div></div>
);
}
