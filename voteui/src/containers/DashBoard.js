import React from 'react';
import NavBar from './NavBar';
import Footer from './Footer';
import './DashBoard.css';


export default function DashBoard() {
    
    return (
        <div className='DashBoard'>
            <NavBar />
            <div className="DashBoard-Content">
          
            </div>
            <Footer />
        </div>
    )
}