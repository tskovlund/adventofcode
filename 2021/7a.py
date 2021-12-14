#!/usr/bin/env python3

import sys
import os
from statistics import median

filename = os.path.basename(__file__).split(".")[0][:-1] + ".txt"
if len(sys.argv) > 1:
    filename = sys.argv[1]

with open(filename) as f:
    line = list(map(int, f.readline().split(",")))
    m = median(line)
    print(int(sum(map(lambda i: abs(i - m), line))))
