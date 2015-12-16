__author__ = 'Filip'

with open('input.txt') as f:
    lines = f.readlines()

ticker_tape = {
    'children': 3,
    'cats': 7,
    'samoyeds': 2,
    'pomeranians': 3,
    'akitas': 0,
    'vizslas': 0,
    'goldfish': 5,
    'trees': 3,
    'cars': 2,
    'perfumes': 1
}

for line in lines:
    split_line = line.replace(':', '').replace(',', '').split(' ')
    nr = split_line[1]
    types = [split_line[i] for i in [2,4,6]]
    amounts = [int(split_line[i]) for i in [3,5,7]]
    for t in zip(types, amounts):
        type = t[0]
        amount = t[1]
        if ticker_tape[type] != amount:
            break
    else:
        print nr
        break
