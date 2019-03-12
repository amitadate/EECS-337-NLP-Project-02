from lxml import html
import requests

def getScrapedData(url):
    tree = html.fromstring(requests.get(url).content)
    recepie_all_data = {}
    nutrition = {}
    recepie_all_data["nutrition"] = nutrition
    recepie_all_data["directions"] = tree.xpath('//span[@class="recipe-directions__list--item"]/text()')
    recepie_all_data["ingredients"] = tree.xpath('//span[@class="recipe-ingred_txt added"]/text()')
    recepie_all_data["nutrition"]["fatContent"] = tree.xpath('//span[@itemprop="fatContent"]/text()')
    recepie_all_data["nutrition"]["carbohydrateContent"] = tree.xpath('//span[@itemprop="carbohydrateContent"]/text()')
    recepie_all_data["nutrition"]["calories"] = tree.xpath('//span[@itemprop="calories"]/text()')
    recepie_all_data["nutrition"]["proteinContent"] = tree.xpath('//span[@itemprop="proteinContent"]/text()')
    recepie_all_data["nutrition"]["sodiumContent"] = tree.xpath('//span[@itemprop="sodiumContent"]/text()')
    return recepie_all_data