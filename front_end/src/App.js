// import logo from './logo.svg';
import React, { useState } from 'react';
import { BrowserRouter as Router, Routes, Route } from 'react-router-dom';
import DishDetails from './DishDetails';
import HomePage from './HomePage';
import DishList from './DishList.js';
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
      const response = await axios.get(`http://localhost:5000/api/recipes?query=${query}`);
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
          <Route path="/" element={!dishes && <HomePage onSearch={handleSearch} /> }/>
          <Route path= "/dishes/:query" element ={dishes && <DishList dishes={dishes} query={searchQuery}/>} />
          <Route path="/dish/:id" element={<DishDetails />} />
        </Routes>
      </div>
  </Router>
  );
};

export default App;
