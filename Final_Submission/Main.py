from url_srapper import getScrapedData
from data_extractor import methods_tools_extracter, ingredients_extracter, nutrition_extracter
from transformer import replace_instructions
from transformation_list import healthy, vegetarian, to_vegan_list
from extracter_list import PRIMARY_COOKING_METHODS, SECONDARY_COOKING_METHODS, ALL_FOOD, TOOLS, UNITS, DESCRIPTOR

food_link1 = "https://www.allrecipes.com/recipe/80827/easy-garlic-broiled-chicken"
print("**********************************************************************************************")
scrapped_data = getScrapedData(food_link1)
print(scrapped_data)

print("**********************************************************************************************")
ingredients = ingredients_extracter(scrapped_data, DESCRIPTOR, UNITS)
print(ingredients)

print("**********************************************************************************************")
nutrition = nutrition_extracter(scrapped_data)
print(nutrition)

print("**********************************************************************************************")
methods = methods_tools_extracter(scrapped_data['directions'], PRIMARY_COOKING_METHODS, SECONDARY_COOKING_METHODS, ALL_FOOD, TOOLS)
print(methods)

print("**********************************************************************************************")
transformed_healthy_method = replace_instructions(methods, healthy)
print(transformed_healthy_method)

print("**********************************************************************************************")
transformed_vegeterian_method = replace_instructions(methods, vegetarian)
print(transformed_vegeterian_method)

print("**********************************************************************************************")
transformed_vegan_method = replace_instructions(methods, to_vegan_list)
print(transformed_vegan_method)