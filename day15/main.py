__author__ = 'Filip'

from itertools import combinations_with_replacement
from operator import mul

def has_500_calories(recipe):
    calorie_list = (calories[ingredient] for ingredient in recipe)
    return sum(calorie_list) == 500

with open('input.txt') as f:
    lines = f.readlines()

properties = {}
calories = {}
property_names = set()
for line in lines:
    ingredient = line.split(': ')[0]
    properties[ingredient] = {}

    property_line = line.split(': ')[-1]
    property_strings = property_line.split(', ')
    for property_string in property_strings:
        property = property_string.split(' ')[0]
        amount = int(property_string.split(' ')[1])
        if not 'calories' in property_string:
            property_names.add(property)
            properties[ingredient][property] = amount
        else:
            calories[ingredient] = amount

recipes = combinations_with_replacement(properties.keys(), 100)
# if question 1, comment out
recipes = (recipe for recipe in recipes if has_500_calories(recipe))

scores = []
for recipe in recipes:
    property_values = {property: 0 for property in property_names}
    for ingredient in recipe:
        for property in property_names:
            property_values[property] += properties[ingredient][property]
    positive_values = [max(0, value) for value in property_values.values()]
    product = reduce(mul, positive_values, 1)
    if product > 0:
        scores.append(product)

print max(scores)


