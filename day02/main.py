__author__ = 'Filip'

with open('input.txt') as f:
    lines = f.readlines()

total_area = 0
total_ribbon = 0
for line in lines:
    dimensions = [int(s) for s in line.split('x')]
    length = dimensions[0]
    width = dimensions[1]
    height = dimensions[2]
    lw = length * width
    wh = width * height
    hl = height * length
    area = 2*lw+2*wh+2*hl+min(lw, wh, hl)
    total_area += area

    sorted_dimensions = sorted(dimensions)
    ribbon_around = 2*sorted_dimensions[0] + 2 * sorted_dimensions[1]
    bow = length*width*height
    total_ribbon += ribbon_around + bow

print total_area
print total_ribbon
