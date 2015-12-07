#!/usr/bin/env python
f = open('input.txt', 'r')
directions = f.read().rstrip('\n')
grid = [(0, 0)]

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

    grid.append((delta_x, delta_y))

    start.update({'x': delta_x, 'y': delta_y})

print(len(set(grid)))
f.close()
