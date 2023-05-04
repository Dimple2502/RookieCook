import React, { useContext } from "react";
import { useParams } from "react-router-dom";
import logo from "../images/logo.png";
import recipeContext from "../contexts/recipeContext";

const Main = () => {
  let { id } = useParams();
  const RecipeContext = useContext(recipeContext);
  const { seasonRecipes } = RecipeContext;

  return (
    <>
      <div className="container">
        <img
          src={logo}
          alt=""
          width="250px"
          height="auto"
          style={{ position: "relative", left: "40%" }}
        />

        <h2>{seasonRecipes[id].RecipeName}</h2>
        <br/>
        <h3>{seasonRecipes[id].Ingredients}</h3>
        <br/>
        <p>
        {seasonRecipes[id].Instructions}
        </p>
      </div>
    </>
  );
};

export default Main;
