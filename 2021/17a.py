#!/usr/bin/env python3

import sys
import os
import numpy as np

filename = os.path.basename(__file__).split(".")[0][:-1] + ".txt"
if len(sys.argv) > 1:
    filename = sys.argv[1]

with open(filename) as f:
    x_range, y_range = map(
        lambda s: tuple(map(int, s.split(".."))),
        f.readline().lstrip("target area: x=").split(", y="),
    )
    
    x = np.roots([1, 1, -2 * x_range[0]])
    if x_range[0] > 0:
        x = int(np.ceil(max(x)))
    else:
        x = int(np.floor(min(x)))

    assert x_range[0] <= x * (x + 1) / 2 <= x_range[1]
    if y_range[0] < 0 and y_range[1] < 0:
        y = -min(y_range) - 1
    print(x, y)
    print(y * (y + 1) // 2)
