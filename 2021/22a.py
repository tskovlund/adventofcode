#!/usr/bin/env python3

import sys
import os
from itertools import product

filename = os.path.basename(__file__).split(".")[0][:-1] + ".txt"
if len(sys.argv) > 1:
    filename = sys.argv[1]

with open(filename) as f:
    on_points = set()
    grid = set(product(range(-50, 51), repeat=3))
    for i, l in enumerate(f):
        print(i)
        on, r = l.strip("\n").split()
        on = on == "on"
        x, y, z = r.split(",")
        x1, x2 = map(int, x[2:].split(".."))
        y1, y2 = map(int, y[2:].split(".."))
        z1, z2 = map(int, z[2:].split(".."))
        c = set(
            product(
                range(max(-50, x1), min(51, x2 + 1)),
                range(max(-50, y1), min(51, y2 + 1)),
                range(max(-50, z1), min(51, z2 + 1)),
            )
        )
        for p in grid:
            if p in c:
                if on:
                    on_points.add(p)
                if not on:
                    on_points.discard(p)
    print(len(on_points))
