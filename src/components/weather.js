import React from "react";
import logo from "../images/logo.png";
import Card from "./card";

const Weather = () => {
    
    let recipes = [
        {
            image : logo,
            title : "Recipe Name 1",
            desc : "Lorem ipsum dolor sit amet consectetur adipisicing elit. Laboriosam, eligendi delectus. Voluptatibus deserunt fugiat labore amet eos, culpa tempora beatae iste temporibus aliquam quae iure minima incidunt consequatur id eaque.",
        },
        {
            image : logo,
            title : "Recipe Name 2",
            desc : "Lorem ipsum dolor sit amet consectetur adipisicing elit. Laboriosam, eligendi delectus. Voluptatibus deserunt fugiat labore amet eos, culpa tempora beatae iste temporibus aliquam quae iure minima incidunt consequatur id eaque.",
        },
        {
            image : logo,
            title : "Recipe Name 3",
            desc : "Lorem ipsum dolor sit amet consectetur adipisicing elit. Laboriosam, eligendi delectus. Voluptatibus deserunt fugiat labore amet eos, culpa tempora beatae iste temporibus aliquam quae iure minima incidunt consequatur id eaque.",
        },
        {
            image : logo,
            title : "Recipe Name 4",
            desc : "Lorem ipsum dolor sit amet consectetur adipisicing elit. Laboriosam, eligendi delectus. Voluptatibus deserunt fugiat labore amet eos, culpa tempora beatae iste temporibus aliquam quae iure minima incidunt consequatur id eaque.",
        },
    ]

    

    return (
        <>
            <div id="weather" className="container">
                <div className="weather">
                    <h2>Seasonal Recipes</h2>
                    <div className="alert alert-warning" role="alert">
                        Its Summer Afternoon!
                    </div>
                    <div className="button-row">
                        <button className="button">Drinks</button>
                        <button className="button">Snacks</button>
                        <button className="button">Main-course</button>
                    </div>
                </div>
                <div className="row row-cols-1 row-cols-md-4 g-4">
                {recipes.map((recipe, index) => {
                    return (
                    <Card key={index} image={recipe.image} title={recipe.title} desc={recipe.desc} />
                    )
                })}
                    </div>
            </div>
        </>
    );
};

export default Weather;
