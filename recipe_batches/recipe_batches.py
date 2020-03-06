#!/usr/bin/python
import math


def recipe_batches(recipe, ingredients):
    batches = math.inf

    '''
    First check to see if there are enough ingredients to satisfy the recipe requirements
    '''
    if len(recipe) > len(ingredients):
        return 0

    '''
      Now check to see if there are enough of each ingredient in the ingredients dictionary.  Since the ingredient order is the same in both dictionaries, we can compare the index values for each against each other
    '''
    for i in recipe:
        if ingredients[i] < recipe[i]:  # if not enough ingredients
            return 0
        # calc batches that can be made for each ingredient
        batch_calc = ingredients[i] // recipe[i]

        # store lowest value of batches possible after each ingredient check
        if batch_calc < batches:
            batches = batch_calc

    return batches


# print(recipe_batches({ 'milk': 100, 'butter': 50, 'cheese': 10 }, { 'milk': 200, 'butter': 100, 'cheese': 10 }))
if __name__ == '__main__':
    # Change the entries of these dictionaries to test
    # your implementation with different inputs
    recipe = {'milk': 100, 'butter': 50, 'flour': 5}
    ingredients = {'milk': 132, 'butter': 48, 'flour': 51}
    print("{batches} batches can be made from the available ingredients: {ingredients}.".format(
        batches=recipe_batches(recipe, ingredients), ingredients=ingredients))
