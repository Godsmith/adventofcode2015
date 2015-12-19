__author__ = 'Filip'

class Replacement:
    def __init__(self, s):
        split_string = s.split(' ')
        self.source = split_string[0]
        self.target = split_string[2][:-1]
        self.num_molecules = sum(1 for c in self.target if c.isupper())

    def __repr__(self):
        return '({}, {}, {})'.format(self.source, self.target, self.num_molecules)

    def replace_backward(self, s):
        return s.replace(self.target, self.source, 1)

with open('input.txt') as f:
    lines = f.readlines()

molecule = lines[-1][:-1]

replacement_strings = lines[:-2]

replacements = []
for s in replacement_strings:
    replacements.append(Replacement(s))

replacements.sort(key=lambda replacement: -replacement.num_molecules)

stepcount = 0
while molecule != 'e':
    for replacement in replacements:
        molecule_before = molecule
        molecule = replacement.replace_backward(molecule)
        if molecule != molecule_before:
            stepcount += 1

    length_last_iteration = len(molecule)

print stepcount



#
# molecules = set()
#
# for source_and_target in replacements:
#     source = source_and_target[0]
#     target = source_and_target[1]
#     for i in range(len(molecule)):
#         molecules.add(molecule[:i] + molecule[i:].replace(source, target, 1))
#
# molecules.remove(molecule)
# print len(molecules)

