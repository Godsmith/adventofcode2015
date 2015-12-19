__author__ = 'Filip'

with open('input.txt') as f:
    lines = f.readlines()

molecule = lines[-1][:-1]

replacement_strings = lines[:-2]

replacements = []
for s in replacement_strings:
    split_string = s.split(' ')
    source = split_string[0]
    target = split_string[2][:-1]
    replacements.append((source, target))

molecules = set()

for source_and_target in replacements:
    source = source_and_target[0]
    target = source_and_target[1]
    for i in range(len(molecule)):
        molecules.add(molecule[:i] + molecule[i:].replace(source, target, 1))

molecules.remove(molecule)
print len(molecules)

