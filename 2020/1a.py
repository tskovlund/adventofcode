import sys
import os

filename = os.path.basename(__file__).split(".")[0][:-1] + ".txt"
if len(sys.argv) > 1:
    filename = sys.argv[1]

with open(filename) as f:
    lines = list(map(int, f.readlines()))
    for i in lines:
        for j in lines:
            if i == j:
                continue
            if i + j == 2020:
                print(i * j)
                sys.exit()
