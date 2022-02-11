import React, { useState } from "react";
import Form from "react-bootstrap/Form";
import Button from "react-bootstrap/Button";
import "./Login.css";

export default function Login() {
const [email, setEmail] = useState("");
const [password, setPassword] = useState("");

function validateForm() {
    return email.length > 0 && password.length > 0;
}

function handleSubmit(event) {
    event.preventDefault();
}

return (
    <div className="Login">
        <div className="head">Welcome To The YearBook!
        <br />
        </div>
        <div className="head2">
        Fill the form below to login
        </div>
        <div className="body">
    <Form onSubmit={handleSubmit}>
        <Form.Group size="lg" controlId="firstname">
        <Form.Label>First name:</Form.Label>
        <br />
        <Form.Control type="text" size="lg"
        placeholder="First name" />
        </Form.Group>
        <div className="description">Enter your first name</div>
        <Form.Group size="lg" controlId="lastname">
        <Form.Label>Last name:</Form.Label>
        <br />
        <Form.Control type="text" 
        placeholder="Last name " />
        </Form.Group>
        <div className="description">Enter your last name</div>
        <Form.Group size="lg" controlId="email">
        <Form.Label>Roll Number </Form.Label>
        <br />
        <Form.Control
            autoFocus
            type="number"
            placeholder="Eg 200020057 1234567891011121314"
            value={email}
            onChange={(e) => setEmail(e.target.value)}
        />
        </Form.Group>
        <div className="description">Enter your roll number: Email will be sent to roll-no@iitb.ac.in</div>
        <Form.Group size="lg" controlId="password">
        <Form.Label>Username (iitbombay.org)</Form.Label>
        <br/>
        <Form.Control
            type="text"
            value={password}
            onChange={(e) => setPassword(e.target.value)}
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
            type="number"
            placeholder="Eg 123456 or leave blank to generate an otp"
            value={email}
            onChange={(e) => setEmail(e.target.value)}
        />
        </Form.Group>
        <div className="description">Enter the 6 digit OTP you recieved on your email (roll-no@iitb.ac.in). Leave blank to Generate a new OTP</div>
        <div className="btn">
        <Button block size="lg" type="submit" disabled={!validateForm()}>
        Generate OTP
        </Button>   
        <Button block size="lg" type="submit" disabled={!validateForm()}>
        Generate OTP
        </Button>
        </div>
        <br/>

    </Form>
    <br/>
    </div>
    </div>
);
}
