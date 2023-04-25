import React from "react";
import logo from "../images/logo.png";
import { Link } from "react-router-dom";
import { useParams,useNavigate } from "react-router-dom";
import ingredients from "../images/Ingredients.png";
import seasonal from "../images/Seasonal.png";
import recipes from "../images/Recipes.png";

const Home = () => {
  const navigate = useNavigate();
  return (
    <>
      <div id="card" className="container">
        <div className="row row-cols-1 row-cols-md-3 g-4">
          <div className="col">
            <div className="card h-100">
              <img src={ingredients} className="card-img-top" alt="" />
              <div className="card-body">
                <h5 className="card-title">Ingredient Identification</h5>
                <p className="card-text">
                  you can scan the igridients you want and identify them by
                  knowing some basic information about them.
                </p>

                <button className="button" onClick={() => {navigate("/object")}}>Lets Go!</button>
              </div>
            </div>
          </div>
          <div className="col">
            <div className="card h-100">
              <img src={seasonal} className="card-img-top" alt="" />
              <div className="card-body">
                <h5 className="card-title">Seasonal Recipes</h5>
                <p className="card-text">
                  you can scan the igridients you want and identify them by
                  knowing some basic information about them.
                </p>

                <button className="button" onClick={() => {navigate("/weather")}}>Lets Go!</button>
              </div>
            </div>
          </div>
          <div className="col">
            <div className="card h-100">
              <img src={recipes} className="card-img-top" alt="" />
              <div className="card-body">
                <h5 className="card-title">Generate Recipe</h5>
                <p className="card-text">
                  you can scan the igridients you want and identify them by
                  knowing some basic information about them.
                </p>

                <button className="button" onClick={() => {navigate("/recipe")}}>Lets Go!</button>
              </div>
            </div>
          </div>
        </div>
      </div>
    </>
  );
};

export default Home;
