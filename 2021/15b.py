#!/usr/bin/env python3

import sys
import os

N = 5

filename = os.path.basename(__file__).split(".")[0][:-1] + ".txt"
if len(sys.argv) > 1:
    filename = sys.argv[1]

with open(filename) as f:
    min_distances = []
    cave = []
    lines = f.readlines()
    count = 0
    for k in range(N):
        for _i, _line in enumerate(lines):
            line = _line.strip("\n")
            n = len(line)
            min_distances.append([0] * N * n)
            cave.append([0] * N * n)
            for l in range(N):
                for _j, _w in enumerate(map(int, line)):
                    i = _i + k * n
                    j = _j + l * n
                    w = _w + k + l
                    if w > 9:
                        w = w % 10 + 1
                    cave[i][j] = w
                    if i > 0:
                        if j > 0:
                            min_prev_distance = min(
                                min_distances[i - 1][j], min_distances[i][j - 1]
                            )
                        else:
                            min_prev_distance = min_distances[i - 1][j]
                    elif j > 0:
                        min_prev_distance = min_distances[i][j - 1]
                    else:
                        min_prev_distance = -w
                    min_distances[i][j] = min_prev_distance + w

    n = len(cave)
    m = min_distances[-1][-1]
    _m = 0
    while _m < m:
        m = min_distances[-1][-1]
        for k in range(2):
            for i in range(n - 1, -1, -1):
                for j in range(n - 1, -1, -1):
                    min_distance = min_distances[i][j]
                    w = cave[i][j]
                    if i < n - 1:
                        min_distance = min(min_distance, w + min_distances[i + 1][j])
                    if j < n - 1:
                        min_distance = min(min_distance, w + min_distances[i][j + 1])
                    min_distances[i][j] = min_distance

            for i in range(n):
                for j in range(n):
                    min_distance = min_distances[i][j]
                    w = cave[i][j]
                    if i > 0:
                        min_distance = min(min_distance, w + min_distances[i - 1][j])
                    if j > 0:
                        min_distance = min(min_distance, w + min_distances[i][j - 1])
                    min_distances[i][j] = min_distance
        _m = min_distances[-1][-1]

    print(min_distances[-1][-1])
