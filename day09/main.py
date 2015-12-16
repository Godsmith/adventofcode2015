__author__ = 'Filip'

from itertools import permutations

with open('input.txt') as f:
    lines = f.readlines()

location_set = set()

for line in lines:
    split_line = line.split(' ')
    location_set.add(split_line[0])
    location_set.add(split_line[2])

locations = list(location_set)

distances = []

for x in range(len(locations)):
    distances.append([])
    for y in range(len(locations)):
        distances[-1].append(10000)

for line in lines:
    split_line = line.split(' ')
    from_location = split_line[0]
    to_location = split_line[2]
    length = int(split_line[4])
    x = locations.index(from_location)
    y = locations.index(to_location)
    distances[x][y] = length
    distances[y][x] = length

lengths = []

for location_list in permutations(locations):
    length = 0
    for i in range(len(location_list) - 1):
        x = locations.index(location_list[i])
        y = locations.index(location_list[i+1])
        length += distances[x][y]

    lengths.append(length)

print min(lengths)
print max(lengths)

