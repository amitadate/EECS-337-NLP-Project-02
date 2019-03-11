from nltk.corpus import wordnet

all_food = list(set([w for s in wordnet.synset('food.n.01').closure(lambda s:s.hyponyms()) for w in s.lemma_names()])) + list(set([w for s in wordnet.synset('food.n.02').closure(lambda s:s.hyponyms()) for w in s.lemma_names()]))

outF = open("all_food.py", "w")
outF.write('", "'.join(all_food))
outF.close()
