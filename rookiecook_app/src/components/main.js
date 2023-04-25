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
          width="200px"
          height="auto"
          style={{ position: "relative", left: "40%" }}
        />

        <h2>{seasonRecipes[id].RecipeName}</h2>
        <br/>
        <h3>{seasonRecipes[id].Ingredients}</h3>
        <br/>
        <p>
          Lorem ipsum dolor, sit amet consectetur adipisicing elit. Nemo nam
          nulla excepturi sequi cum non veritatis, atque nobis, earum blanditiis
          quod odio voluptate dicta incidunt qui magnam tempore ex temporibus.
          Lorem ipsum, dolor sit amet consectetur adipisicing elit. Dolore
          aliquam minus officiis harum labore quod cumque sed, laborum, esse,
          animi repudiandae tempora cupiditate provident culpa alias quisquam
          asperiores magni aspernatur.<br/><br/>
          Lorem ipsum dolor, sit amet consectetur adipisicing elit. Nemo nam
          nulla excepturi sequi cum non veritatis, atque nobis, earum blanditiis
          quod odio voluptate dicta incidunt qui magnam tempore ex temporibus.
          Lorem ipsum, dolor sit amet consectetur adipisicing elit. Dolore
          aliquam minus officiis harum labore quod cumque sed, laborum, esse,
          animi repudiandae tempora cupiditate provident culpa alias quisquam
          asperiores magni aspernatur.
        </p>
      </div>
    </>
  );
};

export default Main;
