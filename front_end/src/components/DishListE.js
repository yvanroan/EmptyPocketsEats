import React from 'react';
import { Link } from 'react-router-dom';

const DishesList = ({ dishes, query, setQuery, onSearch }) => {
    
    const handleSubmit = (event) => {
        event.preventDefault();
        onSearch(query);
    };

  return (
    <div className="dish-list-container">
      <nav className="navbar">
        <h1 className="navbar-title">EmptyPocketsEats</h1>
        <div className="search-section">
          <form onSubmit={handleSubmit} className="">
            <input 
              type="text" 
              value={query} 
              onChange={(e) => setQuery(e.target.value)} 
              placeholder={query} 
              className="search-input"
            />
            
            <button type="submit" className="search-button">Search</button>
          </form>
        </div>
        <ul className="navbar-links">
          <li><Link to="/" className="nav-link">Home</Link></li>
          <li><Link to="/about" className="nav-link">About</Link></li>
          <li><Link to="/contact" className="nav-link">Contact</Link></li>
        </ul>
      </nav>

      <main className="main-content">
        {/* <h2 className="search-results-title">Results for "{query}" </h2> */}
        {dishes ? (
            <ul className="dishes-list">
                {dishes.map(dish => (
                <li key={dish.key} className="dish-item">
                    {dish.image ? <img src={dish.image} alt={dish.title} className="dish-image" /> : <img src="/public/logo192.png" alt={dish.title} className="dish-image" />}
                    <h3 className="dish-title">{dish.title}</h3>
                    {dish.diet.length !=0 ? <p>This meal is considered a {dish.diet.join(', ')} diet.</p> : <p>This meal has a diverse diet.</p>}
                        
                    <a href={dish.url} className="details-link">View Details at {dish.source}</a>
                </li>
                ))}
            </ul>
        ) : (
          <p>Loading...</p>
        )}
      </main>

      <footer className="footer-list">
        <p>© 2023 EmptyPocketsEats. All rights reserved.</p>
      </footer>
    </div>
  );
};

export default DishesList;


