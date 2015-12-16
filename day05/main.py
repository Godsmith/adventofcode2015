_author__ = 'Filip'

with open('input.txt') as f:
    lines = f.readlines()

nice_strings = 0
for line in lines:
    for s in ('ab', 'cd', 'pq', 'xy'):
        if s in line:
            break
    else:
        for i in range(0, len(line) - 1):
            if line[i] == line[i+1]:
                break
        else:
            continue
        vowel_count = 0
        for vowel in 'aeiou':
            vowel_count += line.count(vowel)
            if vowel_count >= 3:
                nice_strings += 1
                print line
                break

print nice_strings
