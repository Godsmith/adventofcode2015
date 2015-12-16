__author__ = 'Filip'

def make_longer(s):
    return s.replace("\\", "\\\\").replace('"','\\"')

with open('input.txt') as f:
    lines = f.readlines()

long_length = len(''.join(lines))

longer_lines = [make_longer(line) for line in lines]

longer_string = '"' + '""'.join(longer_lines) + '"'

longer_length = len(longer_string)

print longer_length - long_length

