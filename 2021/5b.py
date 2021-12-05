import sys
import os
import re

filename = os.path.basename(__file__).split(".")[0][:-1] + ".txt"
if len(sys.argv) > 1:
    filename = sys.argv[1]

with open(filename) as f:
    lines = f.readlines()

    l = []
    min_x = 0
    max_x = 0
    min_y = 0
    max_y = 0
    for i, line in enumerate(lines):
        x1, y1, x2, y2 = map(int, re.split(" -> |,", line[:-1]))

        if i == 0:
            min_x = min(x1, x2)
            max_x = max(x1, x2)
            min_y = min(y1, y2)
            max_y = max(y1, y2)
        min_x = min(min_x, x1, x2)
        max_x = max(max_x, x1, x2)
        min_y = min(min_y, y1, y2)
        max_y = max(max_y, y1, y2)

        l.append(((x1, y1), (x2, y2)))

    intersections = []
    for i in range(min_y, max_y + 1):
        intersections.append([0]*(max_x - min_x + 1))

    count = 0

    for (x1, y1), (x2, y2) in l:
        x1 -= min_x
        x2 -= min_x
        y1 -= min_y
        y2 -= min_y

        if y1 == y2:
            for x in range(min(x1, x2), max(x1, x2) + 1):
                intersections[y1][x] += 1
                if intersections[y1][x] == 2:
                    count += 1

        elif x1 == x2:
            for y in range(min(y1, y2), max(y1, y2) + 1):
                intersections[y][x1] += 1
                if intersections[y][x1] == 2:
                    count += 1

        else:
            if y1 < y2:
                if x1 < x2:
                    for i, y in enumerate(range(y1, y2 + 1)):
                        intersections[y][x1 + i] += 1
                        if intersections[y][x1 + i] == 2:
                            count += 1
                else:
                    for i, y in enumerate(range(y1, y2 + 1)):
                        intersections[y][x1 - i] += 1
                        if intersections[y][x1 - i] == 2:
                            count += 1
            else:
                if x1 < x2:
                    for i, y in enumerate(range(y2, y1 + 1)):
                        intersections[y][x2 - i] += 1
                        if intersections[y][x2 - i] == 2:
                            count += 1
                else:
                    for i, y in enumerate(range(y2, y1 + 1)):
                        intersections[y][x2 + i] += 1
                        if intersections[y][x2 + i] == 2:
                            count += 1

    print(count)
