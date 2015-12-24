__author__ = 'Filip'

values = {'a': 1, 'b': 0}

with open('input.txt') as f:
    lines = f.readlines()

i = 0
while i >= 0 and i < len(lines):
    print values
    print i
    print lines[i]
    split_line = lines[i][:-1].split(' ')
    instruction = split_line[0]
    if instruction == 'hlf':
        values[split_line[1]] /= 2
        i += 1
    elif instruction == 'tpl':
        values[split_line[1]] *= 3
        i += 1
    elif instruction == 'inc':
        values[split_line[1]] += 1
        i += 1
    elif instruction == 'jmp':
        i += int(split_line[1])
    elif instruction == 'jie':
        if values[split_line[1][:-1]] % 2 == 0:
            i += int(split_line[2])
        else:
            i += 1
    elif instruction == 'jio':
        if values[split_line[1][:-1]] == 1:
            i += int(split_line[2])
        else:
            i += 1
    else:
        raise NotImplementedError(instruction)

print values['b']



