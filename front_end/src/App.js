// import logo from './logo.svg';
import React, { useState } from 'react';
import { BrowserRouter as Router, Routes, Route } from 'react-router-dom';
import DishDetails from './components/DishDetails';
import HomePage from './components/HomePage';
// import DishList from './components/DishList';
import DishListE from './components/DishListE';
import axios from 'axios';

const App = () => {
  const [searchQuery, setSearchQuery] = useState('');
  const [dishes, setDishes] = useState(null);

  const handleSearch = async (query) => {
    setSearchQuery(query);
    try {
      // Use Axios when you need to make HTTP requests to an external 
      // resource (like an API). It simplifies the process of making these 
      // requests and handling responses and errors.
      console.log(query)
      const response = await axios.get(`http://localhost:5000/search?query=${query}`);
      console.log(response.data)
      setDishes(response.data); // Assuming the response contains the dish data
    } catch (error) {
      console.error('Error fetching recipes:', error);
    }
  };

  return (
    
    <Router>
      <div>
        <Routes>
          <Route path="/" element={!dishes ? <HomePage onSearch={handleSearch} /> : dishes && <DishListE dishes={dishes} query={searchQuery} setQuery={setSearchQuery} onSearch={handleSearch}/>} />
          <Route path="/dish/:id" element={<DishDetails />} />
        </Routes>
      </div>
  </Router>
  );
};

export default App;
