#!/usr/bin/env python3

import sys
import os

filename = os.path.basename(__file__).split(".")[0][:-1] + ".txt"
if len(sys.argv) > 1:
    filename = sys.argv[1]

with open(filename) as f:
    min_distances = []
    for i, line in enumerate(f):
        line = line.strip("\n")
        min_distances.append([0] * len(line))
        for j, w in enumerate(map(int, line)):
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
    print(min_distances[-1][-1])
