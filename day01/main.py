__author__ = 'Filip'

with open('input.txt') as f:
    text = f.read()

floor = 0
position = 0
for character in text:
    if character == '(':
        floor += 1
    elif character == ')':
        floor -= 1
    position += 1
    if floor < 0:
        print position

print text.count('(') - text.count(')')

