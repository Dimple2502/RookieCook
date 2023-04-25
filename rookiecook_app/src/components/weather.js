import React, { useState, useEffect, useContext } from "react";
import logo from "../images/logo.png";
import Card from "./card";
import recipeContext from "../contexts/recipeContext";

const Weather = () => {
    const RecipeContext = useContext(recipeContext);
    const { fetchRecipe, seasonRecipes } = RecipeContext;

    const date = new Date();
    const month = date.getMonth();
    const hours = date.getHours();

    let season;
    if (month >=10 && month <=2) {
        season = 'Winter';
    } else if (month >=6 && month <=9) {
        season = 'Rainy';
    } else if (month >=3 && month <=5) {
        season = 'Summer';
    } else {
        season = 'Fall';
    }

    let greeting;
    if (hours < 12) {
        greeting = 'Morning';
    } else if (hours >= 12 && hours <= 17) {
        greeting = 'Afternoon';
    } else {
        greeting = 'Evening';
    }

    let recipes = [
        {
            image: logo,
            title: "Recipe Name 1",
            desc: "Lorem ipsum dolor sit amet consectetur adipisicing elit. Laboriosam, eligendi delectus. Voluptatibus deserunt fugiat labore amet eos, culpa tempora beatae iste temporibus aliquam quae iure minima incidunt consequatur id eaque.",
        },
        {
            image: logo,
            title: "Recipe Name 2",
            desc: "Lorem ipsum dolor sit amet consectetur adipisicing elit. Laboriosam, eligendi delectus. Voluptatibus deserunt fugiat labore amet eos, culpa tempora beatae iste temporibus aliquam quae iure minima incidunt consequatur id eaque.",
        },
        {
            image: logo,
            title: "Recipe Name 3",
            desc: "Lorem ipsum dolor sit amet consectetur adipisicing elit. Laboriosam, eligendi delectus. Voluptatibus deserunt fugiat labore amet eos, culpa tempora beatae iste temporibus aliquam quae iure minima incidunt consequatur id eaque.",
        },
        {
            image: logo,
            title: "Recipe Name 4",
            desc: "Lorem ipsum dolor sit amet consectetur adipisicing elit. Laboriosam, eligendi delectus. Voluptatibus deserunt fugiat labore amet eos, culpa tempora beatae iste temporibus aliquam quae iure minima incidunt consequatur id eaque.",
        },
    ]

    useEffect(() => {
        fetchRecipe()
    }, [])

    return (
        <>
            <div id="weather" className="container">
                <div className="weather">
                    <h2>Seasonal Recipes</h2>
                    <div className="alert alert-warning" role="alert">
                        It's {season} {greeting}!
                    </div>
                    {/* <div className="button-row">
                        <button className="button">Drinks</button>
                        <button className="button">Snacks</button>
                        <button className="button">Main-course</button>
                    </div> */}
                </div>
                <div className="row row-cols-1 row-cols-md-4 g-4">
                    {seasonRecipes.map((recipe, index) => {
                        return (
                            <Card key={index} id={index} image={logo} title={recipe.RecipeName} ingredients={recipe.Ingredients} desc={recipe.Instructions} />
                        )
                    })}
                </div>
            </div>
        </>
    );
};

export default Weather;
