import sys
import os

filename = os.path.basename(__file__).split(".")[0][:-1] + ".txt"
if len(sys.argv) > 1:
    filename = sys.argv[1]


def increment(row, col, octo, flashed):
    if (row, col) in flashed:
        return 0
    octo[row][col] = (octo[row][col] + 1) % 10
    count = 0
    if octo[row][col] == 0:
        flashed.add((row, col))
        count += 1
        if row > 0:
            count += increment(row - 1, col, octo, flashed)
            if col > 0:
                count += increment(row - 1, col - 1, octo, flashed)
            if col < 9:
                count += increment(row - 1, col + 1, octo, flashed)
        if row < 9:
            count += increment(row + 1, col, octo, flashed)
            if col > 0:
                count += increment(row + 1, col - 1, octo, flashed)
            if col < 9:
                count += increment(row + 1, col + 1, octo, flashed)
        if col > 0:
            count += increment(row, col - 1, octo, flashed)
        if col < 9:
            count += increment(row, col + 1, octo, flashed)
    return count


with open(filename) as f:
    lines = f.readlines()
    octo = []
    for line in lines:
        octo.append([int(i) for i in line.strip("\n")])
    count = 0
    step = 0
    while count < 100:
        step += 1
        count = 0
        flashed = set()
        for i, row in enumerate(octo):
            for j, col in enumerate(row):
                count += increment(i, j, octo, flashed)
    print(step)
