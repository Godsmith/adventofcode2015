_author__ = 'Filip'

from collections import defaultdict

def has_double_pair(line):
    paircount = defaultdict(list)
    for i in range(0, len(line) - 1):
        pair = line[i:i+2]
        if len(paircount[pair]) == 0:
            paircount[pair].append(i)
        else:
            if paircount[pair][-1] != i - 1:
                return True
    return False

def has_symmetric_letters(line):
    for i in range(0, len(line) - 2):
        if line[i] == line[i+2]:
            return True
    return False



with open('input.txt') as f:
    lines = f.readlines()

nice_strings = 0
for line in lines:
    if has_double_pair(line) and has_symmetric_letters(line):
        nice_strings += 1

print nice_strings

# print has_double_pair('xyxy')
# print has_double_pair('aabcdefgaa')
# print has_double_pair('aaa')
