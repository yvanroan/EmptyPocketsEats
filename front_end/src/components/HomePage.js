import React, { useState } from 'react';

const HomePage = ({ onSearch }) => {
  const [query, setQuery] = useState('');

  const handleSubmit = (event) => {
    event.preventDefault();
    onSearch(query);
  };

  return (
    <div className="home-container">
      <div className="header">
        <h1 className="title">Welcome to EmptyPocketsEats</h1>
        <p className="subtitle">Discover delicious recipes tailored to your taste!</p>
      </div>

      <div className="search-section">
        <form onSubmit={handleSubmit} className="search-form">
          <input 
            type="text" 
            value={query} 
            onChange={(e) => setQuery(e.target.value)} 
            placeholder="Search for recipes..."
            className="search-input"
          />
          
          <button type="submit" className="search-button">Search</button>
        </form>
      </div>

      <div className="footer-home">
        <p className="motto">♪┏(・o･)┛  EmptyPocketsEats: Where Even Our Slogan Is On Ramen Budget   ┗ ( ･o･) ┓♪</p>
      </div>
    </div>
  );
};

export default HomePage;

