from flask import Flask, jsonify
import json
import pandas as pd
import numpy as np
import difflib
import prefer_and_avoid_ingredients 
import string
import weather_detection
# import recipe
from flask_cors import CORS   

app = Flask(__name__)
CORS(app)

# @app.route('/generate-recipes', methods=['POST'])
# def generate_recipes():
#     get_data()
#     return "hello"

@app.route('/suggest-recipes')
def suggest_recipes():
    dummy_response = {
    "recipe": [
        {
        "Ingredients": "1 cup green moong dal - roast, 1/2 cup carrots - peel and chop, 1/2 cup green beans - chop, 1/2 cup cabbage - chop, 1/2 cup green peas, 2 tablespoons coconut - Tighten, 1 teaspoon Ginger - Tighten, 1 teaspoon turmeric powder, 3 dry red chillies, 1 bay leaf, 1 tablespoon cumin seeds, 1 tablespoon ghee, salt - as per taste, 3 cups water, 1/4 teaspoon Cumin seeds, 1/4 teaspoon mustard seeds, 1/4 teaspoon fennel seeds, 1/4 teaspoon Kalonji seeds, 1/4 teaspoon fenugreek seeds, 1/4 teaspoon fenugreek seeds",
        "Instructions": "ओरिया स्टाइल मूंग दालमा बनाने के लिए सबसे पहले मूंग दाल को गरम पानी में आधे घंटे के लिए भिगो ले.अब एक कढ़ाई में दाल को प्रयोग अनुसार पानी के साथ डाले और उनके पक जाने तक पका ले. अब इसमें हल्दी पाउडर, तेज पत्ता, नमक, गाजर, हरे बीन्स, गोभी और मटर डाले। कढ़ाई को ढके और सब्ज़िओ के पकने तक पका ले. बिच बिच में मिलाते रहे. दूसरी कढ़ाई में जीरा और सुखी लाल मिर्च डाले। 1 मिनट तक सेक ले और ठंडा होने के लिए रख दे. ठंडा होने के बाद उन्हें मिक्सर ग्राइंडर में डाले और पीस ले. उसी कढ़ाई में घी हराम करें। इसमें जीरा, राइ, सौंफ, कलोंजी और मेथी के दाने डाले। 15 सेकण्ड्स बाद इसमें अदरक डाले और 1 मिनट तक पका ले. अब इसमें दाल और सब्ज़िओ का मिश्रण डाले और मिला ले. 2 मिनट के लिए पका ले.अंत में नारियल डाले, मिलाए और गैस बंद कर ले. ओरिया स्टाइल मूंग दालमा को चावल और ओरिया स्टाइल घंटा तरकारी के साथ दिन के खाने के लिए परोसे.\n",
        "RecipeName": " Oriya Style Moong Dalma (Recipe In Hindi)"
        },
        {
        "Ingredients": "2 Mango (Ripe) - cut into medium sized cubes,1 tablespoon Coconut Oil,1/2 teaspoon Turmeric powder (Haldi),Salt - to taste,1/2 cup Fresh coconut - grated,1 cup Curd (Dahi / Yogurt) - thick and sour,1/2 teaspoon Cumin seeds (Jeera),3 Green Chillies,1 teaspoon Coconut Oil,1/4 teaspoon Mustard seeds,1/4 teaspoon White Urad Dal (Split),2 sprig Curry leaves,1/2 teaspoon Methi Powder (Fenugreek Powder),2 sprig Curry leaves,2 Dry Red Chillies",
        "Instructions": "To begin with Mambazha Pulissery, in a kadai, add, coconut oil, turmeric powder, salt, mangoes and a cup of water. Cook them over medium flame until the mango pieces become soft.Stir them often to avoid sticking at the bottom of the pan. The gravy becomes thickened once cooled down. Hence, adjust water level as per your required consistency.Once mango pieces are cooked, gently mash them with the back of the ladle.In a mixer, combine coconut, yogurt, cumin seeds, curry leaves add all of them and ground them to fine smooth pasteAdd the grounded paste to the mango gravy and cook over medium flame until the raw smell of the paste leaves, about 8-10 minutes.Switch off the flame and keep the gravy aside.In a small pan, add coconut oil and add mustard seeds, urad dal, curry leaves and wait till the mustard seeds splutter.Add seasoning to the Pulissery. Allow the gravy to settle down for about 20 minutesSeason the gravy with the roasted fenugreek powder at the time of servingServe your Mambazha Pulissery with Steamed Rice, Cabbage And Carrot Thoran Recipe, and Elai Vadam Recipe (A Traditional South Indian Rice Papad) for a complete South Indian meal. \n",
        "RecipeName": "Mambhazam Pulissery Recipe"
        },
        {
        "Ingredients": "1 cup Mango (Ripe) - sweet,2 tablespoons Curd (Dahi / Yogurt),Sugar - as required,1 cup Mango (Raw) - cubes,2 tablespoons Curd (Dahi / Yogurt),2 tablespoons Sugar,1 Green Chilli,Mango (Ripe) - Small cubes of sweet and raw mango cubes",
        "Instructions": "To begin with Sweet And Tangy Mango Ice-cream, we will first begin to prepare the sweet part of the ice cream.For sweet part, mix all the Ingredients mentioned under ’For sweet part’ and blend to a smooth puree in a blender.For tangy part, mix all the Ingredients except curd and give it a churn. Now add curd and blend to a smooth puree.The next step is to assemble the ice cream. Take ice cream moulds, put the raw mango puree and freeze it for about 15 minutes.After 15 minutes, pour sweet mango puree on it. Garnish it with small mango cubes.Insert ice cream sticks in the middle and freeze it for 8 to 10 hours. De-mould it keeping in water for some time and enjoy.Serve Sweet And Tangy Mango Ice-cream as a dessert after your scrumptious meal or you can also serve it to your sudden guests at home.\n",
        "RecipeName": "Sweet And Tangy Mango Ice-cream Recipe"
        },
        {
        "Ingredients": "3 Karela (Bitter Gourd/ Pavakkai),1 Onion - chopped,1 cup Curd (Dahi / Yogurt) - or buttermilk,pinch Turmeric powder (Haldi) - to reduce bitter from bitter gourd,Salt - to taste,1/4 cup Fresh coconut - grated,1/2 teaspoon Mustard seeds,2 Green Chilli,2 teaspoon Coconut Oil,1 teaspoon Mustard seeds,1 Dry Red Chilli,Curry leaves - few",
        "Instructions": "To begin making the Pavakka Pachadi Recipe, first wash the bitter gourd, cut it lengthwise and remove all seeds. Chop it to small pieces.Add 1 teaspoon of salt and a pinch of turmeric powder to bitter gourd slices and mix well. Keep it aside for 30 to 40 minutes. Bitter Gourd would have left some water. Discard it. Again sprinkle little water, mix and squeeze the bitter gourd slices with your hand. This helps to reduce the bitterness of bitter gourd.Heat oil in a heay bottomed pan, add chopped bitter gourd and saute. Keep sauteing in low medium flame. When the bitter gourd is 75% done, add chopped onions and saute . Meanwhile, prepare the masala. Grind coconut, mustard, green chillies and salt to a smooth water adding little water. When the bittergourd and onions are done, add the ground paste to the roasted veggies, add curd or buttermilk . Give a mix and allow it to gently boil on a low medium flame. Switch off. The next step is to prepare the tempering. Heat oil in a tadka pan, add mustard seeds, when it splutters, add red chillies, curry leaves and pour it over the pachadi.Pavakka Pachadi is ready to be savoured! Serve Pavakka Pachadi along with Keerai Sambar, Steamed Rice and Raw Banana Thoran for a delicious everyday meal\n",
        "RecipeName": "Pavakka Pachadi Recipe - Bitter Gourd Pachadi"
        },
        {
        "Ingredients": "2 Nendra Pazham Banana (Ripe) - sliced into rounds,1/4 teaspoon Turmeric powder (Haldi),Salt - to taste,1 cup Curd (Dahi / Yogurt),Coconut Oil - for cooking,1/2 cup Fresh coconut,2 Green Chilli,1 sprig Curry leaves,1 teaspoon Cumin seeds (Jeera),1 teaspoon Mustard seeds,1 sprig Curry leaves,1 teaspoon White Urad Dal (Split),Sunflower Oil - for tempering",
        "Instructions": "To begin making the Nendra Pazham Pulissery Recipe, heat oil in heavy bottomed pan; add the turmeric powder and the Nendra Pazham along with the salt. Stir fry and cook the Nendra Pazham until it is soft and cooked through.Meanwhile grind all the Ingredients - coconut, green chillies, cumin seeds, curry leaves along with 1/2 cup warm water to make a smooth mixture.Add this coconut mixture along with the yogurt to the cooked Nendra Pazham and bring to a brisk boil. Add salt to taste and adjust according to taste. Boil for about 3 to 4 minutes and then turn off the heat.To temper, heat a small tempering pan on heat with oil and add the mustard seeds and allow it to splutter for few seconds and add the curry leaves and the urad dal and allow the dal to turn crisp and golden brown.Once done, turn off the heat and add the seasoning over the Nendra Pazham Pulissery and transfer to a serving bowl and serve hot.Serve the Nendra Pazham Pulissery Recipe along with Steamed Rice, Pavakkai Poriyal Recipe and Elai Vadam for a wholesome lunch or dinner.",
        "RecipeName": "Nendra Pazham Pulissery Recipe - Ayurvedic Recipe"
        },
        {
        "Ingredients": "5 Stalks Lemongrass,3 cloves Garlic,1 inch Ginger,3 Green Chillies - roughly chopped,5 sprigs Coriander (Dhania) Leaves - roughly chopped,2 sprigs Basil leaves - roughly chopped,2 Stalks Spring Onion (Bulb & Greens) - roughly chopped,1 tablespoon Coriander (Dhania) Seeds - roasted,1 teaspoon Whole Black Peppercorns,Salt - to taste,200 ml Dabur Homemade Coconut Milk,1 teaspoon Dabur Homemade Tamarind Paste - dissolved in 2 tablespoons water,1 Thai Green Curry paste - as mention above,1 cup Broccoli - cut into florets,5 Small Brinjal (Baingan / Eggplant) - cut into wedges,1/4 cup Button mushrooms - quartered,1 Red Bell pepper (Capsicum) - diced,1/2 Green zucchini - quartered or sliced,1 cup Vegetable stock,1 tablespoon Brown Sugar (Demerara Sugar),Basil leaves - or kaffir lime leaves,Salt - to taste,1 teaspoon Sunflower Oil - for cooking",
        "Instructions": "Method for Thai Green Curry PasteTo prepare the lemongrass, we will first have to trim away and discard any root section below the bulb base. We will also now remove the dried part of the root until we reach a stage we know that the root cuts easily and is tender. We don't use the leaf part of the lemon grass for the curry paste, you can use it for flavoring a tea or a soup.Continue the same procedure for the remaining lemon grass stalks.Add all the Ingredients for the paste into a blender and a little bit of water. Cover the blender and grind the mixture. After a few seconds of grinding, open the blender and stir to combine the Ingredients and if required add a little more water to grind into a smooth paste.Method to make the Thai Green CurryNext we will proceed to make the Thai Curry with this paste. Heat a teaspoon of oil in a heavy wok. Add in the vegetables.  sprinkle in some salt and stir fry the vegetables on high heat until slightly tender. Once tender turn off the heat and keep aside.Add a teaspoon of oil into the hot wok, next add in 2 to 3 tablespoons of the thai curry paste and saute for a few seconds in the oil. Next add in a cup of water, the tamarind water and stir to combine into the curry.Next we will add in a tablespoon of brown sugar and finally 200 ml of the Dabur coconut milk.Stir to combine all the Ingredients. Once combined, add in the salt, stir and allow the mixture to come to a thicken a little and come to a boilOnce the mixture comes to a boil, add in the torn basil leaves and the stir fried vegetables. Stir the mixture, give it a light boil and the thai curry is ready to be served.Place a cup of steamed rice in a serving bowl. Pour the freshly cooked hot thai vegetarian thai curry on top of the rice until the rice soaks well into the curry and there is enough gravy to soup out and serve immediately to get the best flavors.Serve the Sweet Spicy & Tangy Vegetarian Thai Green Curry along with hot steamed Thai Jasmine Sticky Rice for a simple easy weeknight dinner or even when you have friends over for parties.\n",
        "RecipeName": "Sweet Spicy & Tangy Vegetarian Thai Green Curry Recipe With Tamarind"
        }
    ]
    }
    
    # return dummy_response
    df = pd.read_excel(r'IndianFoodDatasetXLS.xlsx')

    n = len(df)

    list_a = df['TranslatedIngredients'].tolist()
    # print(list_a)


    redundant_words = (['tablespoon','to','cut','into','chop','well','in','tsp','more','warm','frying','original','low','fat','make','the','inch','all','tightly','packed','required','requirement','finely','taste','for','deep','cook','tablespoons','teaspoon','teaspoons','needed','chopped','roughly','cup','cups','salt','to','taste','thinly','as','per','oil','sliced','slice','or','and','halved','half','soaked','overnight','pressure','cooked','coarse','coarsely','pounded','slit','lengthwise','pinch','fresh','wash','grated'])
    list_c = []


    # type(list_a[1])

    for recipe in list_a:
        b = str(recipe).translate(str.maketrans('', '', '/-)(0123456789')).lower() #this line removes punctuation marks other than the commas
        c = str.maketrans(string.punctuation, ' '*len(string.punctuation))  #this line separates buggy seapartion of commas. Example: 'ghee,mango' were treated as a single string. This ;ine removes the commas so that they can be treated differently.
        d = b.translate(c)
        # querywords = d.split()
        # resultwords  = [word for word in querywords if word.lower() not in redundant_words]
        # result = ' '.join(resultwords)
        list_c.append(d)

    list_d = []

    for recipe in list_c:
        Ingredients = recipe.split()
        list_d.append(Ingredients)

    if weather_detection.season == 'summer':
        preferred_ing_list = set(prefer_and_avoid_ingredients.summer_prefer_list) 
        avoided_ing_list = set(prefer_and_avoid_ingredients.summer_avoid_list)


    score_dict = {}
    for i in list_d:
        recipe_score = 0
        for j in i:
            if j not in redundant_words:
                temp_list1 = difflib.get_close_matches(j, preferred_ing_list)
                if len(temp_list1)>0:
                    recipe_score+=1
                temp_list2 = difflib.get_close_matches(j, avoided_ing_list)
                if len(temp_list2)>0:
                    recipe_score-=2

        score_dict[str(list_d.index(i))]=recipe_score

    sorted_score_dict = dict(sorted(score_dict.items(), key=lambda item: item[1]))
    rev_sorted_score_dict = dict(reversed(list(sorted_score_dict.items())))

    suggested_recipes_list = list(rev_sorted_score_dict.keys())

    #getting the top50_recipes
    top50 = []
    for i in suggested_recipes_list:
        if suggested_recipes_list.index(i)<=11:
            top50.append(int(i)+1)

    # return top50
    list_top50_rec_with_data = []
    output = []
    for i in top50:
        # print(f"\n\n{top50.index(i)+1}]\n"+f"{df.loc[i,'TranslatedRecipeName','TranslatedIngredients','TranslatedInstructions']}")
        recipe = df.values[i-1]
        list_top50_rec_with_data.append(recipe)
        recipe_tr_name = recipe[2]
        recipe_tr_ingr = recipe[4]
        recipe_tr_inst = recipe[13]
        recipe_web_link = recipe[14]
        
        # print("\n\n\n############################################")
        # print(f"{top50.index(i)+1}]"+f"{recipe_tr_name}\n")
        # print("Details:")
        # print(f"\n-------Ingredients:--------")
        # print(recipe_tr_ingr)
        # print(f"\n-------Instructions:-------")
        # print(recipe_tr_inst)
        # print("\n-------REFERENCE LINK:------")
        # print(recipe_web_link)              
        recipes = []

        output.append({'RecipeName': recipe_tr_name,
                'Ingredients': recipe_tr_ingr, 
                'Instructions': recipe_tr_inst
                })
        # Serialize the list into JSON
        json_str = jsonify({"recipe":output})

    return (json_str)

if __name__ == '__main__':
    app.run(debug=True)
