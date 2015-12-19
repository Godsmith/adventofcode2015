__author__ = 'Filip'

from itertools import combinations
with open('input.txt') as f:
    lines = f.readlines()

containers = [int(line) for line in lines]

total_combinations = []
for r in range(1, len(containers) + 1):
    total_combinations += combinations(containers, r)

print len(total_combinations)

fitting_combinations = [combination for combination in total_combinations if sum(combination) == 150]

min_length = min([len(combination) for combination in fitting_combinations])

min_length_combinations = [combination for combination in fitting_combinations if len(combination) == min_length]

print len(min_length_combinations)

