import sys
import os

filename = os.path.basename(__file__).split(".")[0][:-1] + ".txt"
if len(sys.argv) > 1:
    filename = sys.argv[1]

with open(filename) as f:
    lines = f.readlines()
    count = 0
    for i in range(len(lines) - 1):
        if int(lines[i + 1]) > int(lines[i]):
            count += 1
    print(count)
