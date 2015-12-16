__author__ = 'Filip'

with open('input.txt') as f:
    lines = f.readlines()

plans = []
for line in lines:
    split_line = line.split(' ')
    speed = int(split_line[3])
    run_time = int(split_line[6])
    rest_time = int(split_line[13])

    time = 0
    plan = []
    while time < 2503:
        plan += [speed] * run_time
        plan += [0] * rest_time
        time += run_time + rest_time
    plans.append(plan)

distances = [0] * len(plans)
points = [0] * len(plans)
for i in range(2503):
    for j in range(len(distances)):
        distances[j] += plans[j][i]
    leading_distance = max(distances)
    for j in range(len(distances)):
        if distances[j] == leading_distance:
            points[j] += 1

print max(distances)
print max(points)


