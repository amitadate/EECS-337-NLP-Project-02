import string

def methods_tools_extracter(directions, PRIMARY_COOKING_METHODS, SECONDARY_COOKING_METHODS, TOOLS, all_food):
    method = {}
    times = ["minutes", "seconds", "hours"]
    for e in directions:
        for j  in e.split("."):
            if "\n" in j:
                continue
            j = j.strip()
            method[j] = {}
            method[j]["Primary method"] = []
            method[j]["Secondary method"] = []
            method[j]["Tools"] = []
            method[j]["Ingredient"] = set() 
            method[j]["Time"] = [] 
            method[j]["Step"] = []
            num = 0
            step = ""
            for i in j.split(" "):
                cur_word = i.lower()
                cur_word = cur_word.strip(string.punctuation)
                if cur_word in PRIMARY_COOKING_METHODS:
                    if cur_word not in method[j]["Primary method"]:
                        method[j]["Primary method"].append(cur_word)
                    step = step + cur_word + " "
                elif cur_word in SECONDARY_COOKING_METHODS:
                    if cur_word not in method[j]["Secondary method"]:
                        method[j]["Secondary method"].append(cur_word) 
                    step = step + cur_word + " "
                elif cur_word in TOOLS:
                    if cur_word not in method[j]["Tools"]:
                        method[j]["Tools"].append(cur_word) 
                    step = step + " in " + cur_word + " "
                elif is_number(cur_word):
                    num = cur_word
                elif cur_word.lower() in times:
                    if int(num) > 0:
                        method[j]["Time"].append(str(num) + " " + cur_word)
                        step = step + " for " + str(num) + " " + cur_word + " "
                        num = 0
                elif cur_word in all_food:
                    method[j]["Ingredient"].add(cur_word)
                    step = step + cur_word + ", "
            method[j]["Step"].append(step.rstrip(', '))
    return method

def is_number(item):
    try:
        float(item)
    except ValueError:
        return False
    return True

def is_fraction(s):
    values = s.split('/')
    return len(values) == 2 and all(i.isdigit() for i in values)

def ingredients_extracter(ingredient_raw_dict, descriptor, units):
    ingredients ={}
    ingredient_list_raw = ingredient_raw_dict['ingredients']
    count=1
    for string in ingredient_list_raw:
        for word in string.split():
            word = word.replace('(', '')
            word = word.replace(')', '')
            word = word.replace(',', '')
            word = word.lower()
            if is_number(word) or is_fraction(word):
                if ('quantity ' + str(count)) in ingredients:
                    ingredients['quantity '+ str(count)] = ingredients['quantity '+ str(count)] + ',' + word
                else:
                    ingredients['quantity '+ str(count)] =  word

            elif word in units:
                if ('measurement ' + str(count)) in ingredients:
                    ingredients['measurement '+ str(count)] = ingredients['measurement '+ str(count)] + ',' + word
                else:
                    ingredients['measurement '+ str(count)] =  word
                
            elif word in descriptor:
                if ('descriptor ' + str(count)) in ingredients:
                    ingredients['descriptor '+ str(count)] = ingredients['descriptor '+ str(count)] + ',' + word
                else:
                    ingredients['descriptor '+ str(count)] =  word
            else: 
                if ('ingredient ' + str(count)) in ingredients:
                    ingredients['ingredient ' + str(count)] = ingredients['ingredient ' + str(count)] +' ' + word
                else:
                    ingredients['ingredient ' + str(count)] =word
        count+=1
    return ingredients

def nutrition_extracter(nutrition):
    nutrition['nutrition']['calories'][0] = nutrition['nutrition']['calories'][0].split(' ')[0]    
    fat_content = float(nutrition['nutrition']['fatContent'][0])
    carbs = float(nutrition['nutrition']['carbohydrateContent'][0])
    calories = float(nutrition['nutrition']['calories'][0])
    protein = float(nutrition['nutrition']['proteinContent'][0])
    sodium = float(nutrition['nutrition']['sodiumContent'][0])
    
    fat_cal = fat_content*9
    carbs_cal = carbs*4
    protein_cal = protein*4
    
    classifications = dict()
    if carbs_cal >= (calories*45/100) and carbs_cal <= (calories*65/100):
        classifications['carbs'] = 'normal'
    elif carbs_cal < (calories*45/100):
        classifications['carbs'] = 'low'
    elif carbs_cal > (calories*65/100):
        classifications['carbs'] = 'high'
        
    if fat_cal >= (calories*20/100) and fat_cal <= (calories*35/100):
        classifications['fat'] = 'normal'
    elif fat_cal < (calories*20/100):
        classifications['fat'] = 'low'
    elif fat_cal > (calories*35/100):
        classifications['fat'] = 'high'
        
    if protein_cal >= (calories*10/100) and protein_cal <= (calories*35/100):
        classifications['protein'] = 'normal'
    elif protein_cal < (calories*10/100):
        classifications['protein'] = 'low'
    elif protein_cal > (calories*35/100):
        classifications['protein'] = 'high'
        
    if sodium >= 140 and sodium <= 400:
        classifications['sodium'] = 'normal'
    elif sodium < 140:
        classifications['sodium'] = 'low'
    elif sodium > 400:
        classifications['sodium'] = 'high'

    return classifications