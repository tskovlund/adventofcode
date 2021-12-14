#!/usr/bin/env python3

import sys
import os

filename = os.path.basename(__file__).split(".")[0][:-1] + ".txt"
if len(sys.argv) > 1:
    filename = sys.argv[1]


with open(filename) as f:
    points = set()
    line = f.readline()
    while "," in line:
        x, y = line.strip("\n").split(",")
        points.add((int(x), int(y)))
        line = f.readline()
    folds = f.readlines()
    for fold in folds:
        axis = fold[11]
        c = int(fold[13:].strip("\n"))
        _points = set()
        for (x, y) in points:
            if axis == "x":
                if x > c:
                    x = 2 * c - x
                _points.add((x, y))
            if axis == "y":
                if y > c:
                    y = 2 * c - y
                _points.add((x, y))
        points = _points
    max_x = max(points, key=lambda p: p[0])[0]
    max_y = max(points, key=lambda p: p[1])[1]
    _points = []
    for i in range(max_y + 1):
        _points.append(["."] * (max_x + 1))
    for (x, y) in points:
        _points[y][x] = "#"
    for line in _points:
        print("".join(line))
