__author__ = 'Filip'

TURN_ON = 0
TURN_OFF = 1
TOGGLE = 3

with open('input.txt') as f:
    lines = f.readlines()

lights = [[0 for x in range(1000)] for y in range(1000)]

for line in lines:
    split_line = line.split(' ')
    if 'turn' in line:
        start_coord = split_line[2]
        stop_coord = split_line[4]
        if split_line[1] == 'on':
            action = TURN_ON
        else:
            action = TURN_OFF
    elif 'toggle' in line:
        start_coord = split_line[1]
        stop_coord = split_line[3]
        action = TOGGLE

    x1, y1 = [int(x) for x in start_coord.split(',')]
    x2, y2 = [int(x) for x in stop_coord.split(',')]

    for x in range(x1, x2+1):
        for y in range(y1, y2+1):
            if action == TURN_ON:
                lights[x][y] += 1
            elif action == TURN_OFF:
                lights[x][y] = max(lights[x][y]-1, 0)
            else:
                lights[x][y] += 2

count = 0
for x in range(1000):
    for y in range(1000):
        count+= lights[x][y]

print count





