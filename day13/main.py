__author__ = 'Filip'

from itertools import permutations

with open('input2.txt') as f:
    lines = f.readlines()

persons = list(set([s.split(' ')[0] for s in lines]))

happiness = {person: {} for person in persons}

for line in lines:
    split_line = line.split(' ')
    person1 = split_line[0]
    person2 = split_line[-1][:-2]
    amount = int(split_line[3])
    if split_line[2] == 'lose':
        amount = -amount

    happiness[person1][person2] = amount

total_happiness = []
for person_list in permutations(persons):
    total_happiness.append(0)
    for i in range(len(person_list)):
        person1 = person_list[i]
        person2 = person_list[(i+1) % (len(person_list))]
        total_happiness[-1] += happiness[person1][person2]
        total_happiness[-1] += happiness[person2][person1]

print max(total_happiness)





