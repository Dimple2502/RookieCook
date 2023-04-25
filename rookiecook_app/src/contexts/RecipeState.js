import React, { useState } from 'react'
import RecipeContext from './recipeContext'

const RecipeState = (props) => {

    const HOST = "http://127.0.0.1:5000";
    const [seasonRecipes, setSeasonRecipes] = useState([{
        "Ingredients": "1 cup green moong dal - roast, 1/2 cup carrots - peel and chop, 1/2 cup green beans - chop, 1/2 cup cabbage - chop, 1/2 cup green peas, 2 tablespoons coconut - Tighten, 1 teaspoon Ginger - Tighten, 1 teaspoon turmeric powder, 3 dry red chillies, 1 bay leaf, 1 tablespoon cumin seeds, 1 tablespoon ghee, salt - as per taste, 3 cups water, 1/4 teaspoon Cumin seeds, 1/4 teaspoon mustard seeds, 1/4 teaspoon fennel seeds, 1/4 teaspoon Kalonji seeds, 1/4 teaspoon fenugreek seeds, 1/4 teaspoon fenugreek seeds",
        "Instructions": "ओरिया स्टाइल मूंग दालमा बनाने के लिए सबसे पहले मूंग दाल को गरम पानी में आधे घंटे के लिए भिगो ले.अब एक कढ़ाई में दाल को प्रयोग अनुसार पानी के साथ डाले और उनके पक जाने तक पका ले. अब इसमें हल्दी पाउडर, तेज पत्ता, नमक, गाजर, हरे बीन्स, गोभी और मटर डाले। कढ़ाई को ढके और सब्ज़िओ के पकने तक पका ले. बिच बिच में मिलाते रहे. दूसरी कढ़ाई में जीरा और सुखी लाल मिर्च डाले। 1 मिनट तक सेक ले और ठंडा होने के लिए रख दे. ठंडा होने के बाद उन्हें मिक्सर ग्राइंडर में डाले और पीस ले. उसी कढ़ाई में घी हराम करें। इसमें जीरा, राइ, सौंफ, कलोंजी और मेथी के दाने डाले। 15 सेकण्ड्स बाद इसमें अदरक डाले और 1 मिनट तक पका ले. अब इसमें दाल और सब्ज़िओ का मिश्रण डाले और मिला ले. 2 मिनट के लिए पका ले.अंत में नारियल डाले, मिलाए और गैस बंद कर ले. ओरिया स्टाइल मूंग दालमा को चावल और ओरिया स्टाइल घंटा तरकारी के साथ दिन के खाने के लिए परोसे.\n",
        "RecipeName": " Oriya Style Moong Dalma (Recipe In Hindi)"
    },])

    const fetchRecipe = async () => {
        const response = await fetch(`${HOST}/suggest-recipes`, {
            method: "GET",
            headers: {
                "Content-Type": "application/json",
            },

        })
        const res = await response.json();
        setSeasonRecipes(res.recipe)
        console.log("receipe data")
        console.log(res.recipe)
    }
    return (
        <RecipeContext.Provider value={{fetchRecipe: fetchRecipe, seasonRecipes: seasonRecipes}}>
            {props.children}
        </RecipeContext.Provider>
    )
}

export default RecipeState