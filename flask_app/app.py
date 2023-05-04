from flask import Flask, jsonify
import json
import pandas as pd
import numpy as np
import difflib
from prefer_and_avoid_ingredients import ingredients
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

# from transformers import T5ForConditionalGeneration, T5Tokenizer

# # Load pre-trained T5 model and tokenizer
# model = T5ForConditionalGeneration.from_pretrained('t5-base')
# tokenizer = T5Tokenizer.from_pretrained('t5-base')

# def generate_recipe(ingredients):
#     # Generate input sequence for the model
#     input_sequence = f"generate a recipe using these ingredients: {','.join(ingredients)} </s>"
    
#     # Encode the input sequence using the tokenizer
#     input_ids = tokenizer.encode(input_sequence, return_tensors='pt')
    
#     # Generate the recipe using the T5 model
#     outputs = model.generate(input_ids=input_ids, max_length=500, num_beams=4, early_stopping=True)
    
#     # Decode the generated recipe and return it as a string
#     recipe = tokenizer.decode(outputs[0], skip_special_tokens=True)
#     return recipe

# @app.route('/test')
# def test():
#     ingredients = ['chicken', 'rice', 'broccoli', 'garlic', 'soy sauce']
#     recipe = generate_recipe(ingredients)
#     print(recipe)
#     return recipe

@app.route('/suggest-recipes')
def suggest_recipes():
    dummy_response = {
  "recipe": [
    {
      "Ingredients": "1 kg Chicken - medium pieces,1/2 cup Mustard oil,Ghee - as required,1-1/2 kg Curd (Dahi / Yogurt),2 inch Cinnamon Stick (Dalchini),2 to 3 Black cardamom (Badi Elaichi),3 to 4 Cloves (Laung),2 teaspoons Asafoetida (hing),2 Bay leaf (tej patta),1 teaspoon Cumin seeds (Jeera),1-1/2 teaspoons Fennel Powder,Salt - as required,1/2 cup Mint Leaves (Pudina) - dry",
      "Instructions": "To begin making the Kashmiri Kokur Yakhni recipe, wash chicken nicely and drain off water.Heat mustard oil in a pressure cooker and add chicken into it along with some salt, fennel powder, crushed big cardamom, asafoetida, cinnamon and bay leaf and fry for 5 minutes on full flame.Put 1/2 a glass of water, stir and pressure-cook upto 1-2 whistles only.Heat some ghee in a wok/kadai and add cumin and cloves into it.Keep the heat low and now add well-whisked curd and turn the flames high. Keep stirring on high flames till it starts to boil. Stir continuously so that the curd doesn't curdle.While the curd is boiling add the chicken along with the spices and left over pure ghee and cook for another 5 to 8 minutes.Once the chicken is nicely cooked, turn off the gas and add lot of crushed dry mint on top.Serve Kashmiri Kokur Yakhni along with Steamed rice and Kachumber Salad for a weekday meal.\n",
      "RecipeName": "Kashmiri Style Kokur Yakhni Recipe-Chicken Cooked In Yogurt"
    },
    {
      "Ingredients": "150 grams Spring Onion (Bulb & Greens) - chopped,3/4 cup Tamarind Water,1 tablespoon Gram flour (besan),2 teaspoons Sunflower Oil,1 teaspoon Mustard seeds,1 teaspoon Cumin seeds (Jeera),2 Dry Red Chillies,1 pinch Asafoetida (hing),1 pinch Turmeric powder (Haldi),Salt - to atste,2 teaspoons Coriander (Dhania) Seeds,1 teaspoon Cumin seeds (Jeera),1/2 teaspoon Mustard seeds,1/4 teaspoon Methi Seeds (Fenugreek Seeds),2 cups Water",
      "Instructions": "To begin making Ullikadala Pulusu Recipe | Spring Onion Curry, in a pan, dry roast coriander seeds, mustard seeds, cumin seeds, fenugreek seeds separately and grind into a fine powder. Keep aside once they are roasted till aromatic.In the same pan, add oil, once it is hot on medium low heat, temper with mustard seeds. Once they splutter, add cumin seeds, red chillies, hing and add spring onions (white part+green part) cut into small pieces. Fry until they turn soft and reduce in size on a low heat.Add about 2 cups of water and bring to boil. Add salt, turmeric, tamarind puree and let it boil for about 2 minutes. In a bowl, mix gramflour and a tablespoon of prepared powder with little water without lumps and add to the boiling mixture. Let it boil for another 2 to 3 minutes and serve. Serve Ullikadala Pulusu Recipe | Spring Onion Curry on a winter day and serve with hot steamed rice and ghee, along with Andhra Gongura Pachadi Recipe, and Andhra Style Kakarakaya Vepudu Recipe (Bitter Gourd Stir Fry).\n",
      "RecipeName": "Ullikadala Pulusu Recipe | Spring Onion Curry"
    },
    {
      "Ingredients": "1 बड़ा चम्मच तेल,1 कप गेहूं का आटा,नमक - स्वाद अनुसार,2 शकरकंदी - छीलकर उबाल ले,1 कप मेथी - काट ले,1 छोटा चम्मच जीरा,1 इंच अदरक - काट ले,1 हरी मिर्च - काट ले,1 छोटा चम्मच हल्दी पाउडर,1 छोटा चम्मच लाल मिर्च पाउडर,1 छोटा चम्मच धनिया पाउडर,2 बड़ा चम्मच सरसों का तेल,नमक - स्वाद अनुसार",
      "Instructions": "शकरकंदी और मेथी का पराठा रेसिपी बनाने के लिए सबसे पहले आलू को प्रेशर कुकर में प्रयोग अनुसार पानी के साथ डाले और 4 सिटी आने तक पका ले. प्रेशर अपने आप निकलने दे.कुकर खोले और आलू को ठंडा होने दे. आलू के ठंडा होने के बाद छिले और मैश कर ले. मेथी को धोकर साफ़ कर ले. मेथी को काटे और अलग से रख दे. अब एक बाउल में गेहूं का आटा, नमक, तेल डाले और मिला ले. थोड़ा थोड़ा पानी डाले और आटे को गुंद ले. ढके और अलग से रख दे. एक कढ़ाई में सरसों का तेल गरम करें। इसमें जीरा डाले और तड़कने दे. अब इसमें अदरक डाले और 2 मिनट के लिए पका ले.अब इसमें मेथी डाले और मेथी के नरम होने तक पका ले. मेथी के नरम होने के बाद आलू, हरी मिर्च, हल्दी पाउडर, लाल मिर्च पाउडर, धनिया पाउडर, नमक डाले और 2 मिनट के लिए पका ले.गैस बंद करें और ठंडा होने के लिए अलग से रख दे. अब आटे का थोड़ा टुकड़ा ले और उसे गोल बेल ले. बिच में मसाले का मिश्रण रखें और चारो तरफ से बंद कर ले. अब इसे सूखे आटे से कोट कर ले. फिर से बेल ले. मोटा मोटा ही बेले वरना मसाला बाहर आ सकता है. ऐसे सारे पराठे बना ले.एक तवा गरम करें। इस पर पराठा डाले और ऊपर से घी लगा ले. दोनों तरफ से सुनहरा भूरा होने तक पकाए और गैस बंद कर ले. शकरकंदी और मेथी का पराठा रेसिपी को बूंदी रायते और मिर्च के अचार के साथ सुबह के नाश्ते या रात के खाने के लिए परोसे।\n",
      "RecipeName": " Sweet Potato & Methi Stuffed Paratha Recipe"
    },
    {
      "Ingredients": "20 बटन मशरुम,2 प्याज - काट ले,1 टमाटर - बारीक काट ले,3 टहनी हरा धनिया - बारीक काट ले,1/2 कप नारियल - कस ले,4 सुखी लाल मिर्च - क्रश कर ले,1 छोटा चम्मच धनिये के बीज,5 पूरी काली मिर्च,2 लॉन्ग,1 छोटा चम्मच हल्दी पाउडर,1 छोटा चम्मच गरम मसाला पाउडर,1/2 इमली - छोटा सा,नमक - स्वाद अनुसार,3 बड़े चम्मच तेल",
      "Instructions": "गोअन मशरुम जकुटी रेसिपी बनाने के लिए सबसे पहले मशरुम को धो ले. काट ले और अलग से रख ले. अब हम जकुटी का पेस्ट बनाएँगे। एक कढ़ाई में तेल गरम करें। इसमें प्याज डाले और उनके नरम होने तक पका ले. प्याज के नरम होने के बाद इसमें धनिये के बीज, सुखी लाल मिर्च, लॉन्ग डाले और 4 से 5 मिनट के लिए पका ले. 4 से 5 मिनट के बाद इसमें नारियल डाले और नारियल के हल्के भूरे होने तक पका ले. गैस बंद कर दे. इसमें इमली, हल्दी पाउडर डाले, मिला ले और ठंडा होने दे. इसमें 1 कप पानी डाले और पीस ले. अलग से रख दे. अब एक कड़ाही में तेल गरम करें। इसमें प्याज डाले और प्याज के नरम होने तक पका ले. होने के बाद इसमें टमाटर डाले और उनके नरम होने तक पका ले. अब इसमें मशरुम डाले और 15 से 20 मिनट के लिए पकने दे. अब इसमें पिसि हुई ग्रेवी का मसाला डाले, मिलाए और 5 से 8 मिनट तक पकने दे. नमक डाले और हरे धनिये से गार्निश करें। गोअन मशरुम जकुटी रेसिपी को लच्छा पराठा और बूंदी रायते के साथ दिन के खाने के लिए परोसे।\n",
      "RecipeName": " Goan Mushroom Xacuti Recipe"
    },
    {
      "Ingredients": "1 cup Quinoa,3/4 cup Sugar,1 teaspoon Cardamom Powder (Elaichi),2 cup Milk - vegans can substitute this ingredient with almond milk,1/2 tablespoon Condensed Milk - or khoya (mawa) vegans can eliminate this ingredient,1/2 tablespoon Ghee,1/4 teaspoon Saffron strands,Mixed nuts - chopped",
      "Instructions": "To begin making Quinoa Phirnee Recipe, place a saucepan on medium heat. Add ghee to it. Once the ghee becomes warm, add quinoa to it. Roast the quinoa till it becomes light brown. At this stage, add 1 cup hot water and bring it to boil. Once the water is reduced to half, add 2 cup hot milk to it. Add the saffron strands to it. Let the quinoa and milk mixture come to boil. Reduce the flame to low and let it simmer for 7-8 minutes. By this time, the quinoa will be perfectly cooked.When the quinoa is cooked through, add sugar and cardamom powder. Stir well and cook until all the sugar dissolves. You can adjust the consistency of the Quinoa Phirnee by adding more hot water if required.Add the condensed milk. Let the mixture simmer for 5 minutes. Turn off the heat.Serve the Quinoa Phirnee Recipe in individual bowls garnished with chopped assorted nuts.You can serve Quinoa Phirnee Recipe warm or chilled.\n",
      "RecipeName": "Quinoa Phirnee Recipe (Quinoa Milk Pudding)"
    },
    {
      "Ingredients": "1-1/2 cup Risotto - cooked risotto (recipe below),1 cup Parmesan cheese - grated,1/2 cup Gorgonzola cheese - cut into 1/4 inch cubes,4 sprig Basil leaves - finely chopped,2 Whole Eggs,2 cups Whole Wheat Bread crumbs - Italian style seasoned,Homemade Pizza And Pasta Sauce - or Marinara Sauce for serving,1 cup Arborio rice,2 cups Vegetable stock - or chicken broth,1/4 cup Butter,1 Onion - finely chopped,1/2 cup Dry white wine,1/2 cup Parmesan cheese - grated,Salt - to taste,Black pepper powder - to taste",
      "Instructions": "To begin making the Italian Arancini Rice Balls Recipe, first we will cook the Risotto.In a saucepan, bring the broth to a simmer and allow it to stay warm on low heat.In a heavy bottomed sauce pan, add the butter and allow it to melt. Saute the onions until lightly cooked and soft.  Add the arborio rice and stir well so it combines with butter. Gradually add the wine a little at a time and simmer until almost all the wine is evaporated. At this stage gradually add the simmering vegetable/ chicken broth and keep stirring until the rice is cooked through. The important trick here is to keep adding 1/4 cup of broth at a time, allow the broth to absorb and evaporate and then proceed to add more to cook the rice. Keep adding it until you feel the risotto is tender and the rice is creamy.Once the rice is cooked through, finally add the parmesan cheese, salt and pepper. Stir it in and saute for a couple of more minutes and turn of the heat.Allow the risotto to cool completely before making the Arancini Rice Balls.In a large mixing bowl, add the cooked risotto, 1 cup of breadcrumbs, parmesan cheese, basil and eggs. With greased hands combine all the ingredients and mash well with your hands. Check the salt and adjust to suit your taste. Take a spoonful of the Arancini rice ball mixture and shape it into 2 inch diameter balls or smaller bite size as desired.Before you shape it completely, place a cube of the Gorgonzola cheese in the center and then seal to make a round ball. Proceed to make the Arancini Rice balls the similar way.Roll the balls in the remaining breadcrumbs to give it a even coating all around.Preheat the oil for deep frying in a deep frying pan.Once the oil is heated on medium heat; add a few Arancini Rice Balls at a time and deep fry them until golden brown. Fry them in small batches, so the oil is able to maintain the even heat. Once done, drain them in paper towels and keep aside for serving.To serve the Arancini Rice Balls, place the Del Monte Pasta Sauce or the Spicy Marinara Sauce in a serving platter and place the rice balls over it and serve immediately.\n",
      "RecipeName": "Italian Arancini Rice Balls Recipe With Delicious Pasta Dipping Sauce"
    },
    {
      "Ingredients": "2 cups Paneer (Homemade Cottage Cheese) - crumbled,4 tablespoons Sugar,1/2 teaspoon Cardamom Powder (Elaichi),Saffron strands - a generous pinch,2 tablespoons Water,1/2 teaspoon Ghee,2 teaspoons Rose water",
      "Instructions": "To begin making the Saffron Paneer Peda recipe, keep the paneer ready. You can either use store bought paneer or make it at home. Follow this Homemade Paneer Recipe to make fresh paneer in your kitchen. Place the  the paneer ina  mixing bowl and crumble it well using your fingers. Transfer this crumbled paneer to the mixer grinder.To the mixer-grinder, add saffron, cardamom powder, sugar and water to it. Grind everything together into a smooth paste.Heat ghee in a heavy bottomed pan on medium-low heat, transfer the paneer mixture from the mixer jar and cook it on low flame.Now add rose water and keep stirring continuously until  everything comes together, leaving the sides of the pan. Turn off the flame, and allow it to cool. Transfer into a bowl. Grease your hands with some ghee and knead the paneer mixture into smooth dough without cracks.Roll the dough flat using rolling pin and cut into desired shape for making pedas. The delicious paneer peda is ready. Transfer to a platter. Serve Saffron Paneer Peda as a dessert after your meal or serve it with some snacks like Poha Chivda to guests when they visit your home during festivals. \n",
      "RecipeName": "Saffron Paneer Peda Recipe"
    },
    {
      "Ingredients": "1/2 cup Onions - chopped,1 cup Soy Chunks (Nuggets) - cooked,1 teaspoon Red Chilli powder,1/4 teaspoon Garam masala powder,4 Spinach Leaves (Palak) - roughly chopped,2 Whole Eggs,2 cloves Garlic,1/2 cup Potatoes (Aloo) - grated,1/3 cup Half and half - (cream and milk),2/3 cup Mozzarella cheese - grated,2 tablespoon Extra Virgin Olive Oil,Salt and Pepper - to taste",
      "Instructions": "To begin making Creamy Spinach And Potato Breakfast Casserole Recipe, get all the ingredients prepped. Grate potatoes, cheese, chop onions, spinach, cook the soya chunks/nuggets.Preheat oven to 400 degrees F.Grease 9 x 8 baking tray or a lasagna pan with some olive oil.In the food processor, add the cooked soya chunks and mince by running the processor a couple of times.Heat a skillet, add olive oil, add grated garlic, saute until the raw smell goes disappears.Add onions and cook until golden. Add the minced soya chunks and stir well to combine.Add chili powder, garam masala with required salt and cook until the mixture is combined well, switch off the stove and let this cool down little bit.In a mixing bowl, add the cooked soya chunks, spinach, eggs, potatoes, milk, cheese with required salt and pepper. Stir well to combine everything well.Add the prepared mixture to the baking tray and bake for about 30-35 minutes or until the top of the dish is golden, springs back when touched on top.Serve Creamy Spinach And Potato Breakfast Casserole Recipe with Chilli Cheese Toast Recipe (Breakfast Bread Pizza) and Mulled Apple Juice Recipe for brunch.\n",
      "RecipeName": "Creamy Spinach And Potato Breakfast Casserole Recipe"
    },
    {
      "Ingredients": "1 cup Rajma (Large Kidney Beans),1 inch Ginger - finely chopped,2 cloves Garlic - finely chopped,1 Onion - roughly chopped,1/2 cup Homemade tomato puree,1 teaspoon Turmeric powder (Haldi),1 teaspoon Cumin powder (Jeera) - roasted,1 teaspoon Garam masala powder,4 Cardamom (Elaichi) Pods/Seeds,2 inch Cinnamon Stick (Dalchini),1 tablespoon Butter,Coriander (Dhania) Leaves - a small bunch,1 teaspoon Sunflower Oil,Salt - to taste",
      "Instructions": "To begin making the Rajma Masala recipe, we will first soak the rajma immersed completely in 3 cups of water for about 8 to 10 hours. To make the Rajma Masala turn on the Preethi Pressure Cooker. Change the setting on the pressure cooker to the saute mode.Heat a teaspoon of oil in the electric pressure cooker pan; add the onion, garlic, ginger and saute for 3 to 4 minutes until the onions start to turn golden in colour.Once done stir in the tomato puree, the turmeric powder, cumin powder, garam masala powder, cardamom pods and cinnamon stick.Saute for another couple of minutes and then add in the soaked rajma along with its water. Add any additional water if required. There should enough water such that the water level is at least 1 inch above the rajma.Cover the pressure cooker, set the mode to rajma mode and wait until done. Once done the electric pressure cooker will go into the keep warm mode. Allow the pressure cooker to release its pressure naturally - you will notice the pressure indicator has gone down.The rajma will continue to cook in the pressure cooker as long as there is pressure inside.Once the pressure has released, open the cooker. The rajma should be now cooked completely. If you press the rajma between your fingers it will get mashed easily.Once the Rajma Masala is cooked, check the salt and spice levels and adjust to suit your taste. Stir in the chopped coriander leaves and serve.Serve the Rajma Masala dish for Sunday Lunch along with Steamed Hot Rice and Aloo Parwal Sabzi making the meal wholesome and nutritious.\n",
      "RecipeName": "One Pot Punjabi Rajma Masala Recipe In Preethi Electric Pressure Cooker"
    },
    {
      "Ingredients": "1 cup All Purpose Flour (Maida),1 teaspoon Baking powder,1/4 teaspoon Baking soda,1/4 teaspoon Salt,3 tablespoons Butter (unsalted) - refrigerated,1/2 cup Buttermilk - cold,2 tablespoons Fresh cream",
      "Instructions": "To begin making the Southern Buttermilk Biscuits recipe, Preheat oven to 450F.Prepare a baking pan. Line it with aluminium foil and grease it.Combine and sieve together flour, baking powder, baking soda and salt into a mixing bowl.Add the cubed butter and mix it till the flour blends well with the butter. Add cold buttermilk intermittently and knead it into a smooth dough. Make sure that the dough is not dry.Using your hands, gently pat the dough out until it is 1/2 inch thickness.Do not use a rolling pin to roll out the dough as it overstimulates the gluten and harden the biscuits.Fold the dough about 4 times and gently press the dough down to a 1 inch thick.Use a round cutter to cut into rounds. You can combine the scraps and gently knead them together to make a small biscuit.Place the biscuits on the prepared pan. Brush the top with cream and bake in the preheated oven for 12 to 15 minutes or until lightly golden brown.Remove from the oven and brush the tops with melted butter. Serve Southern Buttermilk Biscuits with a cup of hot Masala Chai and Masala Oats & Potato Sandwich for a delicious breakfast. You can also serve as a tea time snack.\n",
      "RecipeName": "Southern Buttermilk Biscuits Recipe"
    },
    {
      "Ingredients": "1 बड़ा चम्मच घी,1/4 छोटा चम्मच हींग,1 प्याज - बारीक काट ले,1 इंच अदरक - बारीक काट ले,4 कली लहसुन - बारीक काट ले,2 हरी मिर्च - बारीक काट ले,2 टमाटर - बारीक काट ले,1/2 छोटा चम्मच हल्दी पाउडर,1/2 छोटा चम्मच लाल मिर्च पाउडर,1/2 छोटा चम्मच गरम मसाला पाउडर,नमक - स्वाद अनुसार,1 कप मसूर दाल,2-1/2 कप पानी,हरा धनिया - थोड़ा,1 बड़ा चम्मच घी,1 छोटा चम्मच जीरा,1/4 छोटा चम्मच हींग,1/4 छोटा चम्मच लाल मिर्च पाउडर",
      "Instructions": "तड़के वाली मसूर दाल रेसिपी बनाने के लिए सबसे पहले मसूर दाल को अच्छी तरह से धो कर 3 से 4 घंटे के लिए भिगो दे. एक प्रेशर कुकर में घी गरम करें। इसमें हींग, अदरक, लहसुन, प्याज डाले और प्याज के नरम होने तक पका ले. प्याज के नरम होने के बाद, इसमें टमाटर, हल्दी पाउडर, लाल मिर्च पाउडर, गरम मसाला पाउडर डाले और 1 मिनट के लिए पका ले1 मिनट के बाद इसमें मसूर दाल, नमक और 2-1/2 कप पानी डाले और मिला ले. कुकर बंद करें और 4 सिटी आने तक पका ले. गैस की आंच कम करें और 5 मिनट तक पकने दे. गैस बंद कर दे. प्रेशर अपने आप निकलने दे. प्रेशर निकलने के बाद, कुकर खोले और इसमें हरा धनिया डाले। अब इस मिलाए और एक सर्विंग बाउल में निकाल ले.तड़के के लिए, एक कढ़ाई में घी गरम करें। इसमें जीरा, हींग, लाल मिर्च पाउडर डाले और जीरा के तड़कने तक पकने दे. इस तड़के को दाल में डाले और मिला ले. परोसे।तड़के वाली मसूर दाल रेसिपी को आलू पालक की सब्ज़ी रेसिपी, फुल्का और खमंग ककड़ी के साथ दिन के खाने के लिए परोसे।  \n",
      "RecipeName": " Tadkewali Masoor Dal Recipe"
    },
    {
      "Ingredients": "4 teaspoon Mint powder (Pudina),4 teaspoons Cumin seeds (Jeera) - roasted,1 teaspoon Black pepper powder,2 teaspoon Citric acid crystals,1 pinch Asafoetida (hing),1 teaspoon Dry ginger powder,2 teaspoon Black Salt (Kala Namak),1 teaspoon Amchur (Dry Mango Powder),2 Cardamom (Elaichi) Pods/Seeds - black,2 teaspoon Salt,1 teaspoon Sugar,1/4 teaspoon Fennel seeds (Saunf) - roasted,2 cups Pineapple juice - fresh,1 cup Chilled water,2 teaspoons Jal Jeera Powder - or as needed,2 tablespoon Lemon juice",
      "Instructions": "To begin making the Pineapple Jal Jeera Recipe, in a spice grinder jar, add all the ingredients given under \"For Jal jeera Powder\" which includes mint powder, cumin seeds, black pepper powder, citric acid crystals, asafoetida, dry ginger powder, black salt, amchur, cardamom, salt, sugar, fennel seeds and grind them to a fine powder. Use a dry sleeve/strainer and sleeve the powder once. You can store this powder for later use and use as and when required.In a pitcher, add fresh pineapple juice, cold water, lemon juice with jal jeera powder as needed and stir to combine. Garnish with some mint leaves and serve. Adjust the consistency and taste, by adding more water if required.Serve Pineapple Jal Jeera Recipe during hot summer afternoons as a delicious refreshing evening drink along with snacks like Boti Masala Chaat or Banarasi Tamatar Chaat.\n",
      "RecipeName": "Pineapple Jal Jeera Recipe - Sweet & Sour Pineapple Drink"
    }
  ]
}
    
    # return dummy_response

    ingredients()
    df = pd.read_excel(r'IndianFoodDatasetXLS.xlsx')

    n = len(df)

    list_a = df['TranslatedIngredients'].tolist()

    redundant_words = (['tablespoon','to','cut','into','chop','well','in','tsp','more','warm','frying','original','low','fat','make','the','inch','all','tightly','packed','required','requirement','finely','taste','for','deep','cook','tablespoons','teaspoon','teaspoons','needed','chopped','roughly','cup','cups','salt','to','taste','thinly','as','per','oil','sliced','slice','or','and','halved','half','soaked','overnight','pressure','cooked','coarse','coarsely','pounded','slit','lengthwise','pinch','fresh','wash','grated'])
    list_c = []

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
        recipe = df.values[i-1]
        list_top50_rec_with_data.append(recipe)
        recipe_tr_name = recipe[2]
        recipe_tr_ingr = recipe[4]
        recipe_tr_inst = recipe[13]
        recipe_web_link = recipe[14]

        output.append({'RecipeName': recipe_tr_name,
                'Ingredients': recipe_tr_ingr, 
                'Instructions': recipe_tr_inst
                })
        # Serialize the list into JSON
        json_str = jsonify({"recipe":output})

    return (json_str)

if __name__ == '__main__':
    app.run(debug=True)
