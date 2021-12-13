import sys
import os

filename = os.path.basename(__file__).split(".")[0][:-1] + ".txt"
if len(sys.argv) > 1:
    filename = sys.argv[1]

with open(filename) as f:
    lines = f.readlines()
    count = 0
    for line in lines:
        r, c, p = line.split()
        r_min, r_max = list(map(int, r.split("-")))
        c = c.strip(":")
        p = p.strip("\n")
        if p[r_min - 1] == c and not p[r_max - 1] == c:
            count += 1
        if p[r_min - 1] != c and p[r_max - 1] == c:
            count += 1
    print(count)
