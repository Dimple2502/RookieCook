import React from "react";
import { useState, useContext } from "react";
import { FontAwesomeIcon } from "@fortawesome/react-fontawesome";
import { faSearch, faShoppingCart } from "@fortawesome/free-solid-svg-icons";
import logo from "../images/logo.png";
import recipeContext from "../contexts/recipeContext";
import Card from "./card";

const Recipe = () => {
  const RecipeContext = useContext(recipeContext);
  const { fetchRecipe, seasonRecipes } = RecipeContext;

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
  ];

  const [isOpen, setIsOpen] = useState(false);
  const [selectedIngredients, setSelectedIngredients] = useState([]);
  const [searchTerm, setSearchTerm] = useState("");
  const [cartCount, setCartCount] = useState(0);

  const ingredients = [
    { id: 1, name: "Flour" },
    { id: 2, name: "Sugar" },
    { id: 3, name: "Salt" },
    { id: 4, name: "Eggs" },
    { id: 5, name: "Milk" },
    { id: 6, name: "Butter" },
  ];

  const toggleSidebar = () => {
    setIsOpen(!isOpen);
  };

  const handleSearch = (event) => {
    setSearchTerm(event.target.value);
  };

  const handleIngredientClick = (ingredientId) => {
    const isAlreadySelected = selectedIngredients.includes(ingredientId);
    if (isAlreadySelected) {
      setSelectedIngredients(
        selectedIngredients.filter((id) => id !== ingredientId)
      );
      setCartCount(cartCount - 1);
    } else {
      setSelectedIngredients([...selectedIngredients, ingredientId]);
      setCartCount(cartCount + 1);
    }
  };

  return (
    <>
      <div id="recipe" className="container">
        <div className="recipe">
          <h2>Generate Recipe</h2>
          <div className={`sidebar ${isOpen ? "" : "open"}`}>
            <div className="sidebar-toggle" onClick={toggleSidebar}>
              <i className={`fas ${isOpen ? "fa-times" : "fa-bars"}`} />
            </div>

            <div className="sidebar-header">Ingredients</div>
            {isOpen ? null : (
              <div className="sidebar-search">
                <div className="search-box">
                  <input
                    type="text"
                    placeholder="Search..."
                    value={searchTerm}
                    onChange={handleSearch}
                  />
                  <button>
                    <FontAwesomeIcon icon={faSearch} />
                  </button>
                </div>
              </div>
            )}
            <div className="sidebar-cart">
              <a href="#">
                <FontAwesomeIcon icon={faShoppingCart} />
                <span>Cart ({cartCount})</span>
              </a>
            </div>

            <div className="sidebar-body">
              {ingredients.map((ingredient) => (
                <div
                  key={ingredient.id}
                  className={`ingredient ${selectedIngredients.includes(ingredient.id)
                    ? "selected"
                    : ""
                    }`}
                  onClick={() => handleIngredientClick(ingredient.id)}
                >
                  {ingredient.name}
                </div>
              ))}
            </div>
          </div>
        </div>

        <div className="recipe-card">
          <div className="row row-cols-1 row-cols-md-4 g-4">
            {seasonRecipes.map((recipe, index) => {
              return (
                <Card key={index} id={index} image={logo} title={recipe.RecipeName} ingredients={recipe.Ingredients} desc={recipe.Instructions} />
              )
            })}
          </div>
        </div>
      </div>
    </>
  );
};

export default Recipe;
