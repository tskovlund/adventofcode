#!/usr/bin/env python3

import sys
import os
import numpy as np

filename = os.path.basename(__file__).split(".")[0][:-1] + ".txt"
if len(sys.argv) > 1:
    filename = sys.argv[1]


def gets_within_target_area(vx, vy, x_range, y_range):
    x = 0
    y = 0
    while x <= max(x_range) and y >= min(y_range):
        x += vx
        y += vy
        if min(x_range) <= x <= max(x_range) and max(y_range) >= y >= min(y_range):
            return True
        if vx > 0:
            vx -= 1
        vy -= 1
    return False


with open(filename) as f:
    x_range, y_range = map(
        lambda s: tuple(map(int, s.split(".."))),
        f.readline().lstrip("target area: x=").split(", y="),
    )
    count = 0
    for x in range(1, max(x_range) + 1):
        for y in range(84, min(y_range) - 1, -1):
            if gets_within_target_area(x, y, x_range, y_range):
                count += 1
    print(count)
