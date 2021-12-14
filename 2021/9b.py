#!/usr/bin/env python3

import sys
import os

filename = os.path.basename(__file__).split(".")[0][:-1] + ".txt"
if len(sys.argv) > 1:
    filename = sys.argv[1]


def count_basin(i, j, m, visited=set()):
    rows = len(m)
    cols = len(m[0])
    v = m[i][j]
    count = 1
    if i > 0:
        if m[i - 1][j] > v and m[i - 1][j] < 9:
            if not (i - 1, j) in visited:
                count += count_basin(i - 1, j, m, visited)
                visited.add((i - 1, j))
    if i < rows - 1:
        if m[i + 1][j] > v and m[i + 1][j] < 9:
            if not (i + 1, j) in visited:
                count += count_basin(i + 1, j, m)
                visited.add((i + 1, j))
    if j > 0:
        if m[i][j - 1] > v and m[i][j - 1] < 9:
            if not (i, j - 1) in visited:
                count += count_basin(i, j - 1, m)
                visited.add((i, j - 1))
    if j < cols - 1:
        if m[i][j + 1] > v and m[i][j + 1] < 9:
            if not (i, j + 1) in visited:
                count += count_basin(i, j + 1, m)
                visited.add((i, j + 1))
    return count


with open(filename) as f:
    lines = f.readlines()
    cave_map = []
    for line in lines:
        cave_map.append(list(map(int, line[:-1])))
    low_points = []
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
                low_points.append((i, j))

    max_1 = 0
    max_2 = 0
    max_3 = 0
    for i, j in low_points:
        basin_size = count_basin(i, j, cave_map)
        if basin_size > max_3:
            if basin_size > max_2:
                if basin_size > max_1:
                    max_3 = max_2
                    max_2 = max_1
                    max_1 = basin_size
                else:
                    max_3 = max_2
                    max_2 = basin_size
            else:
                max_3 = basin_size
    print(max_1 * max_2 * max_3)
