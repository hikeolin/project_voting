import React from 'react';


export default function Footer() 
{
    return (
        <div className="Footer p-4 mt-5 bg-light text-dark text-center">
            <span className="text-center">{ new Date().getFullYear()}</span>
        </div>
    ); 
}