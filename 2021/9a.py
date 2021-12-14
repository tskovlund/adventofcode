#!/usr/bin/env python3

import sys
import os

filename = os.path.basename(__file__).split(".")[0][:-1] + ".txt"
if len(sys.argv) > 1:
    filename = sys.argv[1]

with open(filename) as f:
    lines = f.readlines()
    cave_map = []
    for line in lines:
        cave_map.append(list(map(int, line[:-1])))
    print(cave_map)
    risk_levels = 0
    for i, row in enumerate(cave_map):
        for j, col in enumerate(row):
            lowest = True
            if i > 0:
                lowest = lowest and col < cave_map[i - 1][j]
            if i < len(cave_map) - 1:
                lowest = lowest and col < cave_map[i + 1][j]
            if j > 0:
                lowest = lowest and col < row[j - 1]
            if j < len(row) - 1:
                lowest = lowest and col < row[j + 1]
            if lowest:
                risk_levels += col + 1
    print(risk_levels)
