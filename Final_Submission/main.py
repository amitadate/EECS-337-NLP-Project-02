from url_srapper import getScrapedData
from data_extractor import methods_tools_extracter, ingredients_extracter, nutrition_extracter
from transformer import replace_instructions
from transformation_list import healthy, vegetarian, to_vegan_list, normal_to_chinese, x_to_indian, normal_to_indian_utensils, x_to_italian, x_to_mexican, normal_to_chinese_utensils, x_to_non_healthy, x_to_non_veg
from extracter_list import PRIMARY_COOKING_METHODS, SECONDARY_COOKING_METHODS, TOOLS, UNITS, DESCRIPTOR
from all_food import all_food


def func_q(ingredients, nutrition, methods):
    print("\n\n")
    print(" Ingredients :")
    print("\n")
    count = 1
    for key, value in ingredients.items():
        if str(count) in key:
            print("    {} : {} ".format(key.upper(), value))
            continue
        else:
            print("\n")
            print("    {} : {} ".format(key.upper(), value))
            count += 1

    print("\n\n")

    print(" Methods :")
    print("\n")
    for each in methods:
        print("\n * ", each)
        for e in methods[each]:
            if e is "Ingredient":
                continue
            print("   ", e, " - ", ", ".join(methods[each][e]))
    print("\n\n")
    print(" Nutrients :")

    print("\n")

    for key, value in nutrition.items():
        print("    {} : {} ".format(key.upper(), value))

    print("\n\n")
    flag = 0
    return flag


def func_one(methods):
    print("***************************************** Original Scraped Recipie *****************************************************")
    for each in methods:
        print(' *', each)
    print("\n\n")
    print("***************************************** Transformed to Healthy *****************************************************")
    transformed_healthy_method = replace_instructions(methods, healthy)
    print(' * ', end='')
    print("\n * ".join(transformed_healthy_method))
    print("\n\n")
    flag = 0


def func_two(methods):
    print("***************************************** Original Scraped Recipie *****************************************************")
    print('', end='')
    for each in methods:
        print(" *", each)
    print("\n\n")
    print("***************************************** Transformed to Non Healthy ***************************************************")
    transformed_non_healthy_method = replace_instructions(methods, x_to_non_healthy)
    print(' * ', end='')
    print("\n * ".join(transformed_non_healthy_method))
    print("\n\n")
    flag = 0


def func_three(methods):
    print("***************************************** Original Scraped Recipie *****************************************************")
    for each in methods:
        print(" *", each)
    print("\n\n")
    print("***************************************** Transformed to Vegetarian *****************************************************")
    transformed_vegeterian_method = replace_instructions(methods, vegetarian)
    print(' * ', end='')
    print("\n * ".join(transformed_vegeterian_method))
    print("\n\n")
    flag = 0


def func_four(methods):
    print("***************************************** Original Scraped Recipie *****************************************************")
    print('', end='')
    for each in methods:
        print(" *", each)
    print("\n\n")
    print("***************************************** Transformed to Non-Vegetarian *************************************************")
    transformed_non_veg_method = replace_instructions(methods, x_to_non_veg)
    print(' * ', end='')
    print("\n * ".join(transformed_non_veg_method))
    print("\n\n")
    flag = 0


def func_five(methods):
    print("***************************************** Original Scraped Recipie *****************************************************")
    print('', end='')
    for each in methods:
        print(" *", each)
    print("\n\n")
    print("***************************************** Transformed to Vegan *****************************************************")
    transformed_vegan_method = replace_instructions(methods, to_vegan_list)
    print(' * ', end='')
    print("\n * ".join(transformed_vegan_method))
    print("\n\n")
    flag = 0


def func_six(methods):
    print("***************************************** Original Scraped Recipie *****************************************************")
    print('', end='')
    for each in methods:
        print(" *", each)
    print("\n\n")
    print("***************************************** Transformed to Chinese *****************************************************")
    transformed_chinese_method = replace_instructions(methods, normal_to_chinese)
    transformed_chinese_method = replace_instructions(transformed_chinese_method, normal_to_chinese_utensils)
    print(' * ', end='')
    print("\n * ".join(transformed_chinese_method))
    print(" * " + "Sprinkle it with star anise, chinese cinammon and cassia powder")
    print(" * " + "You can make it more delicious by adding hoisin sauce")
    print(" * " + "Also, don't forget to toast with baijiu")
    print("\n\n")
    flag = 0


def func_seven(methods):
    print("***************************************** Original Scraped Recipie *****************************************************")
    print('', end='')
    for each in methods:
        print(" *", each)
    print("\n\n")
    print("***************************************** Transformed to Indian *****************************************************")
    transformed_indian_method = replace_instructions(methods, x_to_indian)
    transformed_indian_method = replace_instructions(transformed_indian_method, normal_to_indian_utensils)
    print(' * ', end='')
    print("\n * ".join(transformed_indian_method))
    print("\n\n")
    flag = 0


def func_eight(methods):
    print("***************************************** Original Scraped Recipie *****************************************************")
    print('', end='')
    for each in methods:
        print(" *", each)
    print("\n\n")
    print("***************************************** Transformed to Mexican *****************************************************")
    transformed_mexican_method = replace_instructions(methods, x_to_mexican)
    print(' * ', end='')
    print("\n * ".join(transformed_mexican_method))
    print("\n\n")
    flag = 0


def func_nine(methods):
    print("***************************************** Original Scraped Recipie *****************************************************")
    print('', end='')
    for each in methods:
        print(" *", each)
    print("\n\n")
    print("***************************************** Transformed to Italian *****************************************************")
    transformed_italian_method = replace_instructions(methods, x_to_italian)
    print(' * ', end='')
    print("\n * ".join(transformed_italian_method))
    print("\n\n")
    flag = 0


def func_ten(methods):
    print("***************************************** Original Scraped Recipie *****************************************************")
    print('', end='')
    for each in methods:
        print(" *", each)
    print("\n\n")
    print("***************************************** Transformed to *****************************************************")
    transformed_healthy_method = replace_instructions(methods, healthy)
    print(' * ', end='')
    print("\n * ".join(transformed_healthy_method))
    print("\n\n")
    flag = 0

def func_yo(url):

    print('--------------------------------')
    print(" URL LOADED : {}".format(url))
    print('--------------------------------')
    #print("****************************************  Scrapped Data  ******************************************************")
    scrapped_data = getScrapedData(url)
    # print(scrapped_data)
    # print("\n")
    print('--------------------------------')
    print(" Data Scraped ")
    print('--------------------------------')
    # print("\n")
    ingredients = ingredients_extracter(scrapped_data, DESCRIPTOR, UNITS)
    # print("\n")
    print('--------------------------------')
    print(" Ingridients Scraped ")
    print('--------------------------------')
    # print("\n")

    nutrition = nutrition_extracter(scrapped_data)
    # print("\n")
    print('--------------------------------')
    print(" Nutrition Scraped ")
    print('--------------------------------')
    # print("\n")

    methods = methods_tools_extracter(scrapped_data['directions'], PRIMARY_COOKING_METHODS, SECONDARY_COOKING_METHODS, TOOLS, all_food)

    # print("\n")
    print('--------------------------------')
    print(" Methods Scraped ")
    print('--------------------------------')
    print("\n")
    print("KINDLY CHOOSE FROM THE FOLLOWING TRANSFORMATIONS BELOW :")
    print('--------------------------------')
        # print("\n")
    return ingredients,nutrition,methods

def default():
    print("\n KINDLY ENTER 0 - 10 or q to EXIT")
    flag = 0


def main():
    flag = 1
    while flag == 1:
        url = ""
        print('\n')
        print(' Enter the URL of the Recipie or Enter " EXIT " to exit the Menu ')
        print('--------------------------------')
        url = input()
        print('--------------------------------')
        if url.lower() != "exit":
            ingredients,nutrition,methods = func_yo(url)
            flag = 0
        if url.lower() == "exit":
            return

        while flag == 0:
            print("\n\n")
            user_input = str(input(" * Enter 0 ----> To view scraped data and Ingridients, Nutrition and Methods\n\n * Enter 1 ----> Transform to Healthy\n\n * Enter 2 ----> Transform to Non-Healthy\n\n * Enter 3 ----> Transform to Vegetarian\n\n * Enter 4 ----> Transform to Non-Vegetarian\n\n * Enter 5 ----> Transform to Vegan\n\n * Enter 6 ----> Transform to Chinese\n\n * Enter 7 ----> Transform to Indian\n\n * Enter 8 ----> Transform to Mexican\n\n * Enter 9 ----> Transform to Italian\n\n * Enter q ----> EXIT back to toggle URL  \n\n * Enter Choice ----> "))
            SWITCH_DICT = {"0": func_q, "1": func_one, "2": func_two, "3": func_three, "4": func_four, "5": func_five, "6": func_six, "7": func_seven, "8": func_eight, "9": func_nine}
            if user_input == "q":
                flag = 1
                break

            if user_input == "0":
                print("\n\n")
                flag = SWITCH_DICT[user_input](ingredients, nutrition, methods)
                flag = 0
            else:
                print("\n\n")
                SWITCH_DICT[user_input](methods)
                flag = 0



if __name__ == '__main__':
    main()
