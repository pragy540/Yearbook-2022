import React from 'react'
import { Navbar, Container, Nav, NavDropdown } from 'react-bootstrap';
import "./css/Navbar.css";
import { BsFillHouseFill, BsImages, BsBarChartLineFill, BsFillPersonFill, BsFillQuestionCircleFill, BsPower } from "react-icons/bs";

const Navbar_func = () => {
  return (
<nav class="navbar navbar-expand-lg navbar-light bg-light main-navbar">
  <div class="container-fluid">
    <a class="navbar-brand" href="#">Yearbook</a>
    <button class="navbar-toggler" type="button" data-bs-toggle="collapse" data-bs-target="#navbarSupportedContent" aria-controls="navbarSupportedContent" aria-expanded="false" aria-label="Toggle navigation">
      <span class="navbar-toggler-icon"></span>
    </button>
    <div class="collapse navbar-collapse middle-links first-links" id="navbarSupportedContent">
      <ul class="navbar-nav me-auto mb-2 mb-lg-0 middle-links">
        <li class="nav-item">
          <a class="nav-link active" aria-current="page" href="#">SARC</a>
        </li>
        <li class="nav-item">
          <a class="nav-link" href="#">IIT Bombay</a>
        </li>

      </ul>
      <form class="d-flex second-links">
        <input class="form-control me-2" type="search" placeholder="Search" aria-label="Search"/>
{/*         <button class="btn btn-outline-success" type="submit">Search</button> */}
      </form>
      <div>
      <ul class="navbar-nav me-auto mb-2 mb-lg-0 third-links">
      <li class="nav-item">
          <a class="nav-link" href="#"><BsFillHouseFill/></a>
        </li>
        <li class="nav-item">
          <a class="nav-link" href="#"><BsImages/></a>
        </li>
        <li class="nav-item">
          <a class="nav-link" href="#"><BsBarChartLineFill/></a>
        </li>
        <li class="nav-item">
          <a class="nav-link" href="#"><BsFillPersonFill/></a>
        </li>
        <li class="nav-item">
          <a class="nav-link" href="#"><BsFillQuestionCircleFill/></a>
        </li>
        <li class="nav-item">
          <a class="nav-link" href="#"><BsPower/></a>
        </li>
      </ul>
      </div>

    </div>
  </div>
</nav>

  
  )
}

export default Navbar_func;