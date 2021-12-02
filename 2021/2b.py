import sys
import os

filename = os.path.basename(__file__).split(".")[0][:-1] + ".txt"
if len(sys.argv) > 1:
    filename = sys.argv[1]

with open(filename) as f:
    lines = f.readlines()
    x = 0
    y = 0
    aim = 0
    for line in lines:
        direction, amount = line.split()
        amount = int(amount)
        if direction == "forward":
            x += amount
            y += amount * aim
        if direction == "down":
            aim += amount
        if direction == "up":
            aim -= amount
    print(x * y)
