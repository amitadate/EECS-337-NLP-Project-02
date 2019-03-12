# EECS-371-NLP-Project-02
Repository for projects undertaken in the course ' Natural Language Processing ' at Northwestern University

## Team Members:

1. Amit Adate [@amitadate](https://github.com/amitadate)
2. Omkar Satpute [@omkarstpt](https://github.com/omkarstpt)
3. Mayank Malik [@mayankmalik01](https://github.com/mayankmalik01)
4. Aditya Kumar [@adijays17](https://github.com/adijays17)

## How to run:
1. To run the code, clone the repo and navigate to Final_Submission folder
2. Create a virtual environment if needed and activate the environment
3. $ pip install -r  requirements.txt
4. Run main.py (to get a menu interface)

Note - In the menu, scroll up to see results displayed or use terminal in fullscreen mode

## Transformations

0) ----> To view scraped data, Ingridients, Nutrition and Methods

1) ----> Transform to Healthy

2) ----> Transform to Non-Healthy

3) ----> Transform to Vegetarain

4) ----> Transform to Non-Vegetarian

5) ----> Transform to Vegan

6) ----> Transform to Chinese

7) ----> Transform to Mexican

8) ----> Transform to Indian

9) ----> Transform to Italian

## Preprocessing

Firstly, we started with Exploratory Data Analsis of most common ingredients used in top recipes of the world. The code for this purpose can be found in **Final_Submission-> PreProcessing**. Using the PreProcessing statistics, we created the list of most common ingredients  and their substitution found in healthy, non healthy, veg, non-veg recipes, chinese, indian, mexican, and itlian recipes.

## Ingredients, Nutritions, and Methods

  Ingredients - name , quantity , measurement (cup, teaspoon, pinch, etc.) , descriptors
  
  Nutritions
  
  Methods:
  Primary cooking method (e.g. sauté, broil, boil, poach, etc.)
  Secondary cooking method (e.g. chop, grate, stir, shake, mince, crush, squeeze, etc.)
  Tools – pans, graters, whisks, etc.
  Steps – parse the directions into a series of steps that each consist of ingredients, tools, methods, and times
