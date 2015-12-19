__author__ = 'Filip'

from copy import deepcopy
GRID_SIDE = 100

def step_all(grid):
    new_grid = deepcopy(grid)
    for x in range(GRID_SIDE):
        for y in range(GRID_SIDE):
            if (x == 0 and y == 0) or (x == 0 and y == GRID_SIDE - 1) or (y == 0 and x == GRID_SIDE - 1) or (x == GRID_SIDE - 1 and y == GRID_SIDE - 1):\
                continue
            neighbours_on = count_neighbours_on(grid, x, y)
            new_grid[x][y] = step_light(grid[x][y], neighbours_on)
    return new_grid

def step_light(status, neighbour_count):
    if status == '#':
        if neighbour_count == 2 or neighbour_count == 3:
            return '#'
    else:
        if neighbour_count == 3:
            return '#'
    return '.'

def count_neighbours_on(grid, x, y):
    count = 0
    for x2 in range(x-1,x+2):
        for y2 in range(y-1,y+2):
            if x2 == x and y2 == y:
                continue
            if x2 < 0 or x2 >= GRID_SIDE or y2 < 0 or y2 >= GRID_SIDE:
                continue
            if grid[x2][y2] == '#':
                count += 1
    return count

with open('input.txt') as f:
    lines = f.readlines()

grid = [list(line[:-1]) for line in lines]

for i in range(100):
    grid = step_all(grid)
print grid
print sum([row.count('#') for row in grid])

