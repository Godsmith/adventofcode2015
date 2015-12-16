__author__ = 'Filip'

from collections import defaultdict

def parse(value):
    if value.isdigit():
        return int(value)
    else:
        return wires[value]

def exists(value):
    return value.isdigit() or value in wires

def all_input_exists(input_list):
    for inp in input_list:
        if not exists(inp):
            return False
    return True

with open('input.txt') as f:
    lines = f.readlines()

wires = defaultdict(int)

while 'a' not in wires:
    for line in lines:
        split_line = line.split(' ')

        destination_wire = split_line[-1][:-1]

        if 'NOT' in line:
            inputs = [split_line[1]]
        elif 'OR' in line or 'AND' in line:
            inputs = [split_line[0], split_line[2]]
        elif 'SHIFT' in line:
            inputs = [split_line[0]]
            shift = int(split_line[2])
        else:
            inputs = [split_line[0]]

        if all_input_exists(inputs):
            if 'NOT' in line:
                wires[destination_wire] = ~parse(inputs[0])
            elif 'OR' in line:
                wires[destination_wire] = parse(inputs[0]) | parse(inputs[1])
            elif 'AND' in line:
                wires[destination_wire] = parse(inputs[0]) & parse(inputs[1])
            elif 'LSHIFT' in line:
                wires[destination_wire] = parse(inputs[0]) << shift
            elif 'RSHIFT' in line:
                wires[destination_wire] = parse(inputs[0]) >> shift
            else:
                wires[destination_wire] = parse(inputs[0])
    print len(wires)
print wires['a']
