import sys
import os
import matplotlib.pyplot as plt

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
        break
    print(len(points))
