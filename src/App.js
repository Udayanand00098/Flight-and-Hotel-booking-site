// App.js
import React from 'react';
import './App.css'; // Assuming you have CSS file for styling
import FlightImage from './Flight.jpg';
import HotelImage from './Hotel.jpg';

function App() {
  return (
    <div className="app">
      <div className="box flight" style={{ backgroundImage: `url(${FlightImage})` }}>
        <div className="content">
          <h2>Book Your Flight</h2>
          <p>Find the best deals on flights to your favorite destinations.</p>
          <button className="bookButton">Book Now</button>
        </div>
      </div>
      <div className="box hotel" style={{ backgroundImage: `url(${HotelImage})` }}>
        <div className="content">
          <h2>Find Your Perfect Hotel</h2>
          <p>Discover the perfect place to stay for your next adventure.</p>
          <button className="bookButton">Book Now</button>
        </div>
      </div>
    </div>
  );
}

export default App;
