#!/usr/bin/python

import math

def recipe_batches(recipe, ingredients):
  batches = math.inf
  if len(recipe) > len(ingredients):
    return 0
  
  for i in recipe:
    # first check if there are enough ingredients
    if ingredients[i] < recipe[i]:
      return 0
    # now calc batches that can be made for each pair  
    batch_calc = ingredients[i] // recipe[i]

    # smallest value is no of total batches possible
    if batch_calc < batches:
      batches = batch_calc

  return batches

# print(recipe_batches({ 'milk': 100, 'butter': 50, 'cheese': 10 }, { 'milk': 200, 'butter': 100, 'cheese': 10 }))
if __name__ == '__main__':
  # Change the entries of these dictionaries to test 
  # your implementation with different inputs
  recipe = { 'milk': 100, 'butter': 50, 'flour': 5 }
  ingredients = { 'milk': 132, 'butter': 48, 'flour': 51 }
  print("{batches} batches can be made from the available ingredients: {ingredients}.".format(batches=recipe_batches(recipe, ingredients), ingredients=ingredients))