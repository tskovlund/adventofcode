import sys
import os

filename = os.path.basename(__file__).split(".")[0][:-1] + ".txt"
if len(sys.argv) > 1:
    filename = sys.argv[1]

with open(filename) as f:
    lines = list(map(int, f.readlines()))
    for i in lines:
        for j in lines:
            for k in lines:
                if i == j or i == k or j == k:
                    continue
                if i + j + k == 2020:
                    print(i * j * k)
                    sys.exit()
