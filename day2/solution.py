#!/usr/bin/env python
f = open('input.txt', 'r')
dimensions = f.readlines()
paper_needed = 0

for dimension in dimensions:
    int_dimensions = map(lambda x: int(x), dimension.rstrip('\n').split('x'))
    int_dimensions.sort()
    paper_needed += (lambda short, medium, lng: short*medium + 2*short*medium + 2*medium*lng + 2*short*lng)(*int_dimensions)

print(paper_needed)
f.close()
