#!/usr/bin/python

import math
#function that receives a recipe in the form of a dictionary

def recipe_batches(recipe, ingredients):

    if len(list(dict.values(recipe))) is not len(list(dict.values(ingredients))):
        return 0
    total_recipes_completed = None
    for val in recipe:
        total = ingredients[val] // recipe[val]
        if total_recipes_completed is None:
            total_recipes_completed = total
        elif total < total_recipes_completed:
            total_recipes_completed = total
    return total_recipes_completed


if __name__ == '__main__':
  # Change the entries of these dictionaries to test 
  # your implementation with different inputs
  recipe = { 'milk': 30, 'butter': 30, 'flour': 30 }
  ingredients = { 'milk': 132, 'butter': 48, 'flour': 51 }
  print("{batches} batches can be made from the available ingredients: {ingredients}.".format(batches=recipe_batches(recipe, ingredients), ingredients=ingredients))