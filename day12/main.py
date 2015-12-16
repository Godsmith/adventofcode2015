__author__ = 'Filip'

import json

number_sum = 0

def parse(object):
    global number_sum
    if type(object) is list:
        for i in object:
            parse(i)
    if type(object) is dict:
        for i in object.values():
            parse(i)
    if type(object) is int:
        number_sum += object



with open('input.txt') as f:
    doc = json.load(f)

parse(doc)

print number_sum
