__author__ = 'Filip'

from collections import defaultdict

with open('input.txt') as f:
    fulltext = f.read()

presents = defaultdict(int)

for text in [fulltext[0::2], fulltext[1::2]]:
    x = 0
    y = 0
    for character in text:
        if character == '<':
            x -= 1
        if character == 'v':
            y += 1
        if character == '>':
            x += 1
        if character == '^':
            y -= 1
        presents[str(x) + ',' + str(y)] += 1

print len(presents)
