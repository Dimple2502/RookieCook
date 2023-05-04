import React from "react";
import { useState, useContext } from "react";
import { FontAwesomeIcon } from "@fortawesome/react-fontawesome";
import { faSearch, faShoppingCart } from "@fortawesome/free-solid-svg-icons";
import axios from "axios";
import logo from "../images/logo.png";
import recipeContext from "../contexts/recipeContext";
import Card from "./card";

const Recipe = () => {
  const RecipeContext = useContext(recipeContext);
  const { fetchRecipe, seasonRecipes } = RecipeContext;

  // let recipes = [
  //   {
  //     image: logo,
  //     title: "Recipe Name 1",
  //     desc: "Lorem ipsum dolor sit amet consectetur adipisicing elit. Laboriosam, eligendi delectus. Voluptatibus deserunt fugiat labore amet eos, culpa tempora beatae iste temporibus aliquam quae iure minima incidunt consequatur id eaque.",
  //   },
  //   {
  //     image: logo,
  //     title: "Recipe Name 2",
  //     desc: "Lorem ipsum dolor sit amet consectetur adipisicing elit. Laboriosam, eligendi delectus. Voluptatibus deserunt fugiat labore amet eos, culpa tempora beatae iste temporibus aliquam quae iure minima incidunt consequatur id eaque.",
  //   },
  //   {
  //     image: logo,
  //     title: "Recipe Name 3",
  //     desc: "Lorem ipsum dolor sit amet consectetur adipisicing elit. Laboriosam, eligendi delectus. Voluptatibus deserunt fugiat labore amet eos, culpa tempora beatae iste temporibus aliquam quae iure minima incidunt consequatur id eaque.",
  //   },
  //   {
  //     image: logo,
  //     title: "Recipe Name 4",
  //     desc: "Lorem ipsum dolor sit amet consectetur adipisicing elit. Laboriosam, eligendi delectus. Voluptatibus deserunt fugiat labore amet eos, culpa tempora beatae iste temporibus aliquam quae iure minima incidunt consequatur id eaque.",
  //   },
  // ];

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


  function showRecipeSteps(instructions) {
    const parser = new DOMParser();
    const html = parser.parseFromString(instructions, "text/html");
    const listItems = html.querySelectorAll("ol li");
    let steps = "";
    listItems.forEach((item) => {
      steps += item.textContent + "\n";
    });
    const ingredientsList = steps.map((ingredient) => ingredient.value);
    return ingredientsList;
  }

  const [ingredientsApi, setIngredientsApi] = useState("");
  const [recipe, setRecipe] = useState(null);
  const apiKey = "8c0970efe939476c8658755d2da4d3e9"; // replace with your Spoonacular API key

  const handleSubmit = async (e) => {
    e.preventDefault();
    try {
      const responsedata = [
        {
          "id": 632583,
          "title": "Apple Pie with PB&J Streusel",
          "image": "https://spoonacular.com/recipeImages/632583-312x231.jpg",
          "imageType": "jpg",
          "usedIngredientCount": 2,
          "missedIngredientCount": 4,
          "missedIngredients": [
            {
              "id": 2010,
              "amount": 0.75,
              "unit": "teaspoon",
              "unitLong": "teaspoons",
              "unitShort": "tsp",
              "aisle": "Spices and Seasonings",
              "name": "cinnamon",
              "original": "3/4 teaspoon cinnamon",
              "originalName": "cinnamon",
              "meta": [],
              "image": "https://spoonacular.com/cdn/ingredients_100x100/cinnamon.jpg"
            },
            {
              "id": 9152,
              "amount": 1.0,
              "unit": "tablespoon",
              "unitLong": "tablespoon",
              "unitShort": "Tbsp",
              "aisle": "Produce",
              "name": "lemon juice",
              "original": "1 tablespoon lemon juice",
              "originalName": "lemon juice",
              "meta": [],
              "image": "https://spoonacular.com/cdn/ingredients_100x100/lemon-juice.jpg"
            },
            {
              "id": 2025,
              "amount": 4.0,
              "unit": "g",
              "unitLong": "grams",
              "unitShort": "g",
              "aisle": "Spices and Seasonings",
              "name": "nutmeg",
              "original": "1/2 teaspoon nutmeg (4 g)",
              "originalName": "1/2 teaspoon nutmeg",
              "meta": [],
              "image": "https://spoonacular.com/cdn/ingredients_100x100/ground-nutmeg.jpg"
            },
            {
              "id": 1145,
              "amount": 6.0,
              "unit": "tablespoons",
              "unitLong": "tablespoons",
              "unitShort": "Tbsp",
              "aisle": "Milk, Eggs, Other Dairy",
              "name": "butter",
              "original": "3/4 stick (6 tablespoons) unsalted butter, melted",
              "originalName": "3/4 stick unsalted butter, melted",
              "meta": [
                "unsalted",
                "melted"
              ],
              "extendedName": "unsalted butter",
              "image": "https://spoonacular.com/cdn/ingredients_100x100/butter-sliced.jpg"
            }
          ],
          "usedIngredients": [
            {
              "id": 1109003,
              "amount": 1.0,
              "unit": "",
              "unitLong": "",
              "unitShort": "",
              "aisle": "Produce",
              "name": "gala apple",
              "original": "1 gala apple",
              "originalName": "gala apple",
              "meta": [],
              "image": "https://spoonacular.com/cdn/ingredients_100x100/apple.jpg"
            },
            {
              "id": 1089003,
              "amount": 1.0,
              "unit": "",
              "unitLong": "",
              "unitShort": "",
              "aisle": "Produce",
              "name": "granny smith apple",
              "original": "1 granny smith apple",
              "originalName": "granny smith apple",
              "meta": [],
              "image": "https://spoonacular.com/cdn/ingredients_100x100/grannysmith-apple.png"
            }
          ],
          "unusedIngredients": [],
          "likes": 1
        }, {
          "id": 640352,
          "title": "Cranberry Apple Crisp",
          "image": "https://spoonacular.com/recipeImages/640352-312x231.jpg",
          "imageType": "jpg",
          "usedIngredientCount": 1,
          "missedIngredientCount": 3,
          "missedIngredients": [
            {
              "id": 9078,
              "amount": 2.0,
              "unit": "cups",
              "unitLong": "cups",
              "unitShort": "cup",
              "aisle": "Produce",
              "name": "cranberries",
              "original": "2 cups fresh cranberries",
              "originalName": "fresh cranberries",
              "meta": [
                "fresh"
              ],
              "extendedName": "fresh cranberries",
              "image": "https://spoonacular.com/cdn/ingredients_100x100/cranberries.jpg"
            },
            {
              "id": 1145,
              "amount": 4.0,
              "unit": "Tbs",
              "unitLong": "Tbs",
              "unitShort": "Tbs",
              "aisle": "Milk, Eggs, Other Dairy",
              "name": "butter",
              "original": "1/2 stick (4 Tbs) unsalted butter, cut into cubes",
              "originalName": "1/2 stick unsalted butter, cut into cubes",
              "meta": [
                "unsalted",
                "cut into cubes"
              ],
              "extendedName": "unsalted butter",
              "image": "https://spoonacular.com/cdn/ingredients_100x100/butter-sliced.jpg"
            },
            {
              "id": 8120,
              "amount": 1.5,
              "unit": "cups",
              "unitLong": "cups",
              "unitShort": "cup",
              "aisle": "Cereal",
              "name": "regular oats",
              "original": "1 1/2 cups regular oats (not quick-cooking)",
              "originalName": "regular oats (not quick-cooking)",
              "meta": [
                "(not quick-cooking)"
              ],
              "image": "https://spoonacular.com/cdn/ingredients_100x100/rolled-oats.jpg"
            }
          ],
          "usedIngredients": [
            {
              "id": 1089003,
              "amount": 4.0,
              "unit": "cups",
              "unitLong": "cups",
              "unitShort": "cup",
              "aisle": "Produce",
              "name": "granny smith apples",
              "original": "4 cups Granny Smith apples, chopped into ½ inch chunks",
              "originalName": "Granny Smith apples, chopped into ½ inch chunks",
              "meta": [
                "chopped"
              ],
              "image": "https://spoonacular.com/cdn/ingredients_100x100/grannysmith-apple.png"
            }
          ],
          "unusedIngredients": [],
          "likes": 11
        }
      ]
      
      const recipeIddata = responsedata[0].id;
      const recipeResponsedata = {
        "vegetarian": true,
        "vegan": false,
        "glutenFree": false,
        "dairyFree": false,
        "veryHealthy": false,
        "cheap": false,
        "veryPopular": false,
        "sustainable": false,
        "lowFodmap": false,
        "weightWatcherSmartPoints": 88,
        "gaps": "no",
        "preparationMinutes": -1,
        "cookingMinutes": -1,
        "aggregateLikes": 1,
        "healthScore": 17,
        "creditsText": "Foodista.com – The Cooking Encyclopedia Everyone Can Edit",
        "license": "CC BY 3.0",
        "sourceName": "Foodista",
        "pricePerServing": 190.77,
        "extendedIngredients": [
          {
            "id": 19334,
            "aisle": "Baking",
            "image": "light-brown-sugar.jpg",
            "consistency": "SOLID",
            "name": "brown sugar",
            "nameClean": "golden brown sugar",
            "original": "1/4 cup brown sugar",
            "originalName": "brown sugar",
            "amount": 0.25,
            "unit": "cup",
            "meta": [],
            "measures": {
              "us": {
                "amount": 0.25,
                "unitShort": "cups",
                "unitLong": "cups"
              },
              "metric": {
                "amount": 59.147,
                "unitShort": "ml",
                "unitLong": "milliliters"
              }
            }
          },
          {
            "id": 2010,
            "aisle": "Spices and Seasonings",
            "image": "cinnamon.jpg",
            "consistency": "SOLID",
            "name": "cinnamon",
            "nameClean": "cinnamon",
            "original": "3/4 teaspoon cinnamon",
            "originalName": "cinnamon",
            "amount": 0.75,
            "unit": "teaspoon",
            "meta": [],
            "measures": {
              "us": {
                "amount": 0.75,
                "unitShort": "tsps",
                "unitLong": "teaspoons"
              },
              "metric": {
                "amount": 0.75,
                "unitShort": "tsps",
                "unitLong": "teaspoons"
              }
            }
          },
          {
            "id": 20081,
            "aisle": "Baking",
            "image": "flour.png",
            "consistency": "SOLID",
            "name": "flour",
            "nameClean": "wheat flour",
            "original": "3 cups all-purpose flour",
            "originalName": "all-purpose flour",
            "amount": 3.0,
            "unit": "cups",
            "meta": [
              "all-purpose"
            ],
            "measures": {
              "us": {
                "amount": 3.0,
                "unitShort": "cups",
                "unitLong": "cups"
              },
              "metric": {
                "amount": 709.764,
                "unitShort": "ml",
                "unitLong": "milliliters"
              }
            }
          },
          {
            "id": 1109003,
            "aisle": "Produce",
            "image": "apple.jpg",
            "consistency": "SOLID",
            "name": "gala apple",
            "nameClean": "gala apple",
            "original": "1 gala apple",
            "originalName": "gala apple",
            "amount": 1.0,
            "unit": "",
            "meta": [],
            "measures": {
              "us": {
                "amount": 1.0,
                "unitShort": "",
                "unitLong": ""
              },
              "metric": {
                "amount": 1.0,
                "unitShort": "",
                "unitLong": ""
              }
            }
          },
          {
            "id": 1089003,
            "aisle": "Produce",
            "image": "grannysmith-apple.png",
            "consistency": "SOLID",
            "name": "granny smith apple",
            "nameClean": "granny smith apple",
            "original": "1 granny smith apple",
            "originalName": "granny smith apple",
            "amount": 1.0,
            "unit": "",
            "meta": [],
            "measures": {
              "us": {
                "amount": 1.0,
                "unitShort": "",
                "unitLong": ""
              },
              "metric": {
                "amount": 1.0,
                "unitShort": "",
                "unitLong": ""
              }
            }
          },
          {
            "id": 9152,
            "aisle": "Produce",
            "image": "lemon-juice.jpg",
            "consistency": "LIQUID",
            "name": "lemon juice",
            "nameClean": "lemon juice",
            "original": "1 tablespoon lemon juice",
            "originalName": "lemon juice",
            "amount": 1.0,
            "unit": "tablespoon",
            "meta": [],
            "measures": {
              "us": {
                "amount": 1.0,
                "unitShort": "Tbsp",
                "unitLong": "Tbsp"
              },
              "metric": {
                "amount": 1.0,
                "unitShort": "Tbsp",
                "unitLong": "Tbsp"
              }
            }
          },
          {
            "id": 2025,
            "aisle": "Spices and Seasonings",
            "image": "ground-nutmeg.jpg",
            "consistency": "SOLID",
            "name": "nutmeg",
            "nameClean": "nutmeg",
            "original": "1/2 teaspoon nutmeg (4 g)",
            "originalName": "1/2 teaspoon nutmeg",
            "amount": 4.0,
            "unit": "g",
            "meta": [],
            "measures": {
              "us": {
                "amount": 0.141,
                "unitShort": "oz",
                "unitLong": "ounces"
              },
              "metric": {
                "amount": 4.0,
                "unitShort": "g",
                "unitLong": "grams"
              }
            }
          },
          {
            "id": 2047,
            "aisle": "Spices and Seasonings",
            "image": "salt.jpg",
            "consistency": "SOLID",
            "name": "salt",
            "nameClean": "table salt",
            "original": "1/4 teaspoon salt",
            "originalName": "salt",
            "amount": 0.25,
            "unit": "teaspoon",
            "meta": [],
            "measures": {
              "us": {
                "amount": 0.25,
                "unitShort": "tsps",
                "unitLong": "teaspoons"
              },
              "metric": {
                "amount": 0.25,
                "unitShort": "tsps",
                "unitLong": "teaspoons"
              }
            }
          },
          {
            "id": 19335,
            "aisle": "Baking",
            "image": "sugar-in-bowl.png",
            "consistency": "SOLID",
            "name": "sugar",
            "nameClean": "sugar",
            "original": "2 cups sugar",
            "originalName": "sugar",
            "amount": 2.0,
            "unit": "cups",
            "meta": [],
            "measures": {
              "us": {
                "amount": 2.0,
                "unitShort": "cups",
                "unitLong": "cups"
              },
              "metric": {
                "amount": 473.176,
                "unitShort": "ml",
                "unitLong": "milliliters"
              }
            }
          },
          {
            "id": 1145,
            "aisle": "Milk, Eggs, Other Dairy",
            "image": "butter-sliced.jpg",
            "consistency": "SOLID",
            "name": "butter",
            "nameClean": "unsalted butter",
            "original": "3/4 stick (6 tablespoons) unsalted butter, melted",
            "originalName": "3/4 stick unsalted butter, melted",
            "amount": 6.0,
            "unit": "tablespoons",
            "meta": [
              "unsalted",
              "melted"
            ],
            "measures": {
              "us": {
                "amount": 6.0,
                "unitShort": "Tbsps",
                "unitLong": "Tbsps"
              },
              "metric": {
                "amount": 6.0,
                "unitShort": "Tbsps",
                "unitLong": "Tbsps"
              }
            }
          },
          {
            "id": -1,
            "aisle": "?",
            "image": null,
            "consistency": "SOLID",
            "name": "tropical foods pb&j mix",
            "nameClean": null,
            "original": "¼ cup Tropical Foods PB&J mix, rough chopped",
            "originalName": "Tropical Foods PB&J mix, rough chopped",
            "amount": 0.25,
            "unit": "cup",
            "meta": [
              "chopped"
            ],
            "measures": {
              "us": {
                "amount": 0.25,
                "unitShort": "cups",
                "unitLong": "cups"
              },
              "metric": {
                "amount": 59.147,
                "unitShort": "ml",
                "unitLong": "milliliters"
              }
            }
          }
        ],
        "id": 632583,
        "title": "Apple Pie with PB&J Streusel",
        "readyInMinutes": 45,
        "servings": 2,
        "sourceUrl": "http://www.foodista.com/recipe/3WLJQBDB/apple-pie-with-pb-j-streusel",
        "image": "https://spoonacular.com/recipeImages/632583-556x370.jpg",
        "imageType": "jpg",
        "summary": "You can never have too many American recipes, so give Apple Pie with PB&J Streusel a try. This recipe serves 2 and costs $1.91 per serving. This dessert has <b>1967 calories</b>, <b>20g of protein</b>, and <b>38g of fat</b> per serving. From preparation to the plate, this recipe takes around <b>45 minutes</b>. This recipe from Foodista has 1 fans. If you have granny smith apple, galan apple, flour, and a few other ingredients on hand, you can make it. It is a good option if you're following a <b>lacto ovo vegetarian</b> diet. All things considered, we decided this recipe <b>deserves a spoonacular score of 59%</b>. This score is pretty good. If you like this recipe, take a look at these similar recipes: <a href=\"https://spoonacular.com/recipes/apple-pie-streusel-cake-565640\">Apple Pie Streusel Cake</a>, <a href=\"https://spoonacular.com/recipes/apple-pear-streusel-pie-265449\">Apple-Pear Streusel Pie</a>, and <a href=\"https://spoonacular.com/recipes/caramel-apple-streusel-pie-559616\">Caramel Apple Streusel Pie</a>.",
        "cuisines": [
          "American"
        ],
        "dishTypes": [
          "dessert"
        ],
        "diets": [
          "lacto ovo vegetarian"
        ],
        "occasions": [],
        "winePairing": {
          "pairedWines": [
            "prosecco",
            "moscato dasti",
            "late harvest riesling"
          ],
          "pairingText": "Apple Pie works really well with Prosecco, Moscato d'Asti, and Late Harvest Riesling. These dessert wines have the right amount of sweetness and light, fruity flavors that won't overpower apple pie. The Ruffino Prosecco Made with Organic Grapes with a 4.8 out of 5 star rating seems like a good match. It costs about 22 dollars per bottle.",
          "productMatches": [
            {
              "id": 490182,
              "title": "Ruffino Prosecco Made with Organic Grapes",
              "description": "The bouquet is fragrant and bursting with fruit notes. It has clean aromas of apples, pears, and citrus, accompanied by hints of wisteria. Crisp, clean, and delicate with fine bubbles on the palate. Intense flavors of apple and peach lead to a pleasant finish with lingering fruit and floral notes.",
              "price": "$21.99",
              "imageUrl": "https://spoonacular.com/productImages/490182-312x231.jpg",
              "averageRating": 0.96,
              "ratingCount": 5.0,
              "score": 0.8975,
              "link": "https://click.linksynergy.com/deeplink?id=*QCiIS6t4gA&mid=2025&murl=https%3A%2F%2Fwww.wine.com%2Fproduct%2Fruffino-prosecco-made-with-organic-grapes%2F596419"
            }
          ]
        },
        "instructions": "<ol><li>Preheat oven to 425 degrees.</li><li>Peel and slice apples into quarter sized slices.</li><li>Toss apples in cinnamon, nutmeg, lemon juice, sugar and salt; let sit.</li><li>Mix all ingredients for streusel together.</li><li>Fill a greased small baking dish with apple mixture.</li><li>Top with streusel and bake until streusel is brown.</li></ol>",
        "analyzedInstructions": [
          {
            "name": "",
            "steps": [
              {
                "number": 1,
                "step": "Preheat oven to 425 degrees.Peel and slice apples into quarter sized slices.Toss apples in cinnamon, nutmeg, lemon juice, sugar and salt; let sit.",
                "ingredients": [
                  {
                    "id": 9152,
                    "name": "lemon juice",
                    "localizedName": "lemon juice",
                    "image": "lemon-juice.jpg"
                  },
                  {
                    "id": 2010,
                    "name": "cinnamon",
                    "localizedName": "cinnamon",
                    "image": "cinnamon.jpg"
                  },
                  {
                    "id": 9003,
                    "name": "apple",
                    "localizedName": "apple",
                    "image": "apple.jpg"
                  },
                  {
                    "id": 2025,
                    "name": "nutmeg",
                    "localizedName": "nutmeg",
                    "image": "ground-nutmeg.jpg"
                  },
                  {
                    "id": 19335,
                    "name": "sugar",
                    "localizedName": "sugar",
                    "image": "sugar-in-bowl.png"
                  },
                  {
                    "id": 2047,
                    "name": "salt",
                    "localizedName": "salt",
                    "image": "salt.jpg"
                  }
                ],
                "equipment": [
                  {
                    "id": 404784,
                    "name": "oven",
                    "localizedName": "oven",
                    "image": "oven.jpg"
                  }
                ]
              },
              {
                "number": 2,
                "step": "Mix all ingredients for streusel together.Fill a greased small baking dish with apple mixture.Top with streusel and bake until streusel is brown.",
                "ingredients": [
                  {
                    "id": 9003,
                    "name": "apple",
                    "localizedName": "apple",
                    "image": "apple.jpg"
                  }
                ],
                "equipment": [
                  {
                    "id": 404646,
                    "name": "baking pan",
                    "localizedName": "baking pan",
                    "image": "roasting-pan.jpg"
                  },
                  {
                    "id": 404784,
                    "name": "oven",
                    "localizedName": "oven",
                    "image": "oven.jpg"
                  }
                ]
              }
            ]
          }
        ],
        "originalId": null,
        "spoonacularSourceUrl": "https://spoonacular.com/apple-pie-with-pb-j-streusel-632583"
      }
      let response = await axios.get(`https://api.spoonacular.com/recipes/findByIngredients?apiKey=${apiKey}&ingredients=${ingredientsApi}&number=1&ranking=1`);
      let recipeId = response.data[0].id;
      let recipeResponse = await axios.get( `https://api.spoonacular.com/recipes/${recipeId}/information?apiKey=${apiKey}`);
      setRecipe(recipeResponse.data);
      console.log(response);
      console.log(recipeId);
      console.log(recipeResponse);
    } catch (error) {
      console.error(error);
      setRecipe(null);
    }
  };




  return (
    <>
      <div id="recipe" className="container">
        <div className="recipe">
          <h2>Generate Recipe</h2><br/>
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

        {/* <div className="recipe-card">
          <div className="row row-cols-1 row-cols-md-4 g-4">
            {seasonRecipes.map((recipe, index) => {
              return (
                <Card key={index} id={index} image={logo} title={recipe.RecipeName} ingredients={recipe.Ingredients} desc={recipe.Instructions} />
              )
            })}
          </div>
        </div> */}
        <div className="container" style={{display: "flex", justifyContent: "center"}}>
          <form>
            <label htmlFor="ingredients">Enter ingredients:</label>
            <input
              type="text"
              id="ingredients"
              value={ingredientsApi}
              onChange={(e) => setIngredientsApi(e.target.value)}
            />
            <button type="submit" style={{marginTop: "10%"}} onClick={handleSubmit}>Generate Recipe</button>
          <div style={{marginTop: "10%"}}>
          {recipe ? (
            <div>
              <h2>{recipe.title}</h2>
          <ol dangerouslySetInnerHTML={{ __html: recipe.instructions }}></ol>
              
            </div>
          ) : (
            <p>No recipe found.</p>
            )}
            </div>
            </form>
        </div>
      </div>
    </>
  );
};

export default Recipe;
