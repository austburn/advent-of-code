#!/usr/bin/env python
f = open('input.txt', 'r')
dimensions = f.readlines()
paper_needed = 0

for dimension in dimensions:
    # Translate '2x6x4\n' => [2, 6, 4]
    int_dimensions = map(lambda x: int(x), dimension.rstrip('\n').split('x'))
    # Sort it so we know what the smallest side is
    int_dimensions.sort()
    # Honestly, just some lambda experimentation
    # We now have [2, 4, 6], so we need to add short*medium (smallest side) to the total surface area
    paper_needed += (lambda short, medium, lng: short*medium + 2*short*medium + 2*medium*lng + 2*short*lng)(*int_dimensions)

print(paper_needed)
f.close()
