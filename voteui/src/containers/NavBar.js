import React from "react";
import { Navbar, Nav } from "react-bootstrap";
import "./NavBar.css";

export default function NavBar(props) {

  function handleSignOut(event) {
    console.log(event.target);
  }

  return (
    <div className="NavBar">      
        <Navbar collapseOnSelect  expand="lg" fixed="top" bg="light" variant="light">
          <Navbar.Brand>Polls</Navbar.Brand>
          <Navbar.Toggle aria-controls="nav-section"/>
          <Navbar.Collapse id="nav-section" className="justify-content-end">
              <Nav.Link href="/polls/active" className="mr-sm-2">Active</Nav.Link>
              <Nav.Link href="./polls/archived" className="mr-sm-3">Archived</Nav.Link>
              <Nav.Link onClick={handleSignOut}>Logout</Nav.Link>
          </Navbar.Collapse>  
        </Navbar>
    </div>
  );

}