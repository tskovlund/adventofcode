#!/usr/bin/env python3

import sys
import os

filename = os.path.basename(__file__).split(".")[0][:-1] + ".txt"
if len(sys.argv) > 1:
    filename = sys.argv[1]

with open(filename) as f:
    lines = f.readlines()
    count = 0
    for line in lines:
        line = line.split(" | ")[1].split()
        for output in line:
            if len(output) in [2, 3, 4, 7]:
                count += 1

print(count)
