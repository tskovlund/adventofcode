import sys
import os

filename = os.path.basename(__file__).split(".")[0][:-1] + ".txt"
if len(sys.argv) > 1:
    filename = sys.argv[1]

with open(filename) as f:
    lines = list(map(int, f.readlines()))
    count = 0
    for i in range(len(lines) - 3):
        if sum(lines[i+1:i+4]) > sum(lines[i:i+3]):
            count += 1
    print(count)
