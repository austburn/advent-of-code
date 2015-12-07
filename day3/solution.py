#!/usr/bin/env python
f = open('input.txt', 'r')
directions = f.read().rstrip('\n')
grid = {
    0: {
        0: 1
    }
}

ops = {
    '>': (1, 0),
    '<': (-1, 0),
    '^': (0, 1),
    'v': (0, -1)
}
start = {
    'x': 0,
    'y': 0
}

for direction in directions:
    op = ops[direction]
    delta_x = op[0] + start['x']
    delta_y = op[1] + start['y']

    try:
        grid[delta_x]
    except:
        grid[delta_x] = {}

    row = grid[delta_x]

    try:
        row[delta_y] += 1
    except:
        row[delta_y] = 1

    start.update({'x': delta_x, 'y': delta_y})

houses = 0
for row in grid:
    houses += len(grid[row].keys())

print(houses)
f.close()
