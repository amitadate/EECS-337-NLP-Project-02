# from nltk.corpus import wordnet
# import pickle
# from all_food import all_food
# all_food = list(set([w for s in wordnet.synset('food.n.01').closure(lambda s:s.hyponyms()) for w in s.lemma_names()])) + list(set([w for s in wordnet.synset('food.n.02').closure(lambda s:s.hyponyms()) for w in s.lemma_names()]))

# outF = open("all_food.py", "w")
# outF.write('", "'.join(all_food))
# outF.close()

# with open("all_food.py", "wb") as fp:   #Pickling
#     pickle.dump(all_food, fp)
# with open("all_food.py", "rb") as fp:   # Unpickling
#     b = pickle.load(fp)