import React, { useState } from 'react';
import Routes from "./Routes";

function App() {

  const [isAuthenticated, setIsAuthenticated] = useState(false);
  const props = { isAuthenticated };
  
  return (
    <div className="App">
      <Routes appProps={props}/>
    </div>
  );
}

export default App;
