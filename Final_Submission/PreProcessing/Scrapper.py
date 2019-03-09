from lxml import html
from urls import VEG
from data_extractor import ingredients_extracter
from extracter_list import UNITS, DESCRIPTOR
import requests

def scrape_ingrdients(urls):
    def get_name(ingredients):
        all_ingredient  = []
        for each in ingredients:
            if each.startswith('name'):
                all_ingredient.append(ingredients[each])
        return all_ingredient
    all_ingrdeients = []
    for url in urls:
        recepie_all_data = {}
        tree = html.fromstring(requests.get(url).content)
        recepie_all_data["ingredients"] = tree.xpath('//span[@class="recipe-ingred_txt added"]/text()')
        all_ingrdeients = all_ingrdeients + get_name(ingredients_extracter(recepie_all_data, DESCRIPTOR, UNITS))
    return all_ingrdeients

with open('veg.txt', 'w') as f:
    for item in scrape_ingrdients(VEG):
        f.write("%s\n" % item)
