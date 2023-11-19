// App.js (React Frontend)


// Example React component
import React, { useState, useEffect } from 'react';
import axios from 'axios';

const RecipesList = () => {
    const [recipes, setRecipes] = useState([]);

    useEffect(() => {
        axios.get('http://localhost:5000/api/recipes')
            .then(response => {
                setRecipes(response.data);
            })
            .catch(error => {
                console.error('There was an error fetching the recipes:', error);
            });
    }, []); // Empty dependency array ensures this runs once after component mounts

    return (
        <div>
            {recipes.map(recipe => (
                <div key={recipe.id}>
                    <h2>{recipe.title}</h2>
                    {/* Render other recipe details */}
                </div>
            ))}
        </div>
    );
}

export default RecipesList;

