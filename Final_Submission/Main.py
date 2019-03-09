from url_srapper import getScrapedData
from data_extractor import methods_tools_extracter, ingredients_extracter, nutrition_extracter
from transformer import replace_instructions
from transformation_list import healthy, vegetarian, to_vegan_list, normal_to_chinese
from extracter_list import PRIMARY_COOKING_METHODS, SECONDARY_COOKING_METHODS, TOOLS, UNITS, DESCRIPTOR

food_link1 = "https://www.allrecipes.com/recipe/222000/spaghetti-aglio-e-olio"
print("****************************************  Scrapped Data  ******************************************************")
scrapped_data = getScrapedData(food_link1)
print(scrapped_data)
print("\n\n")

print("***************************************** Ingredients *****************************************************")
ingredients = ingredients_extracter(scrapped_data, DESCRIPTOR, UNITS)
print(ingredients)
print("\n\n")

print("******************************************** Nutrients **************************************************")
nutrition = nutrition_extracter(scrapped_data)
print(nutrition)
print("\n\n")

print("******************************************** Methods **************************************************")
methods = methods_tools_extracter(scrapped_data['directions'], ingredients, PRIMARY_COOKING_METHODS, SECONDARY_COOKING_METHODS, TOOLS)
print('', end='')
for each in methods:
    print("\n * ", each)
    for e in methods[each]: 
        print("   ", e, " - ", ", ".join(methods[each][e]))
print("\n\n")

print("***************************************** Transformed to Healthy *****************************************************")
transformed_healthy_method = replace_instructions(methods, healthy)
print(' * ', end='')
print("\n * ".join(transformed_healthy_method))
print("\n\n")

print("***************************************** Transformed to Vegetarian *****************************************************")
transformed_vegeterian_method = replace_instructions(methods, vegetarian)
print(' * ', end='')
print("\n * ".join(transformed_vegeterian_method))
print("\n\n")

print("****************************************** Transformed to Vegan ****************************************************")
transformed_vegan_method = replace_instructions(methods, to_vegan_list)
print(' * ', end='')
print("\n * ".join(transformed_vegan_method))
print("\n\n")

print("****************************************** Transformed to Chinese ****************************************************")
transformed_chinese_method = replace_instructions(methods, normal_to_chinese)
print(' * ', end='')
print("\n * ".join(transformed_chinese_method))
print("\n\n")
