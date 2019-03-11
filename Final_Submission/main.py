from url_srapper import getScrapedData
from data_extractor import methods_tools_extracter, ingredients_extracter, nutrition_extracter
from transformer import replace_instructions
from transformation_list import healthy, vegetarian, to_vegan_list, normal_to_chinese, x_to_indian, x_to_italian, x_to_mexican, normal_to_chinese_utensils, x_to_non_healthy, x_to_non_veg
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
    print(" Nutrients :")

    print("\n")

    for key, value in nutrition.items():
        print("    {} : {} ".format(key.upper(), value))

    print("\n\n")
    print(" Methods :")
    for each in methods:
        print("\n * ", each)
        for e in methods[each]:
            if e is "Ingredient":
                continue
            print("   ", e, " - ", ", ".join(methods[each][e]))
    print("\n\n")


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


def func_seven(methods):
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


def func_eight(methods):
    print("***************************************** Original Scraped Recipie *****************************************************")
    print('', end='')
    for each in methods:
        print(" *", each)
    print("\n\n")
    print("***************************************** Transformed to Indian *****************************************************")
    transformed_indian_method = replace_instructions(methods, x_to_indian)
    print(' * ', end='')
    print("\n * ".join(transformed_indian_method))
    print("\n\n")


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


def default():
    print("\n KINDLY ENTER 1 - 9 or 0 to EXIT")


def main():

    url = ""
    while url.lower() != "exit":
        print(' Enter the URL of the Recipie or Enter " EXIT " to exit the Menu ')
        print('--------------------------------')
        url = input()
        print('--------------------------------')
        if url.lower() != "exit":

            while True:
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

                user_input = str(input("Enter a ----> To view scraped data and Ingridients, Nutrition and Methods\n\nEnter 1 ----> Transform to Healthy\n\nEnter 2 ----> Transform to Non-Healthy\n\nEnter 3 ----> Transform to Vegetarian\n\nEnter 4 ----> Transform to Non-Vegetarian\n\nEnter 5 ----> Transform to Vegan\n\nEnter 6 ----> Transform to Chinese\n\nEnter 7 ----> Transform to Mexican\n\nEnter 8 ----> Transform to Indian\n\nEnter 9 ----> Transform to Italian\n\nEnter 0 ----> EXIT back to toggle URL  "))
                if user_input == "0":
                    break
                else:
                    SWITCH_DICT = {"a": func_q, "1": func_one, "2": func_two, "3": func_three, "4": func_four, "5": func_five, "6": func_six, "7": func_seven, "8": func_eight, "9": func_nine}
                    if user_input == "a":
                        SWITCH_DICT[user_input](ingredients, nutrition, methods)
                    else:
                        SWITCH_DICT[user_input](methods)

    return


if __name__ == '__main__':
    main()
