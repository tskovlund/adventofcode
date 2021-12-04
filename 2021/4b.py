import sys
import os

filename = os.path.basename(__file__).split(".")[0][:-1] + ".txt"
if len(sys.argv) > 1:
    filename = sys.argv[1]

plates_won = set()


def print_score(plate, n):
    score = 0
    for line in plate:
        for number, flag in line:
            if not flag:
                score += int(number)
    score *= int(n)
    print(score)


def has_won(plate, i, j):
    won_row = True
    for number, flag in plate[i]:
        won_row = flag and won_row
    won_col = True
    for line in plate:
        won_col = line[j][1] and won_col
    return won_row or won_col


def check_plate(plate, n):
    for i, line in enumerate(plate):
        for j, (m, f) in enumerate(line):
            if m == n:
                plate[i][j] = (m, True)
                if has_won(plate, i, j):
                    print_score(plate, n)
                    return True


def check_plates(plates, n):
    for i, plate in enumerate(plates):
        if not i in plates_won:
            if check_plate(plate, n):
                plates_won.add(i)


with open(filename) as f:
    numbers = f.readline()[:-1].split(",")
    lines = f.readlines()
    plates = []
    for i in range(0, len(lines), 6):
        plate_lines = lines[i + 1 : i + 6]
        plate = []
        for line in plate_lines:
            plate.append([(i, False) for i in line.strip("\n").split()])
        plates.append(plate)
    for n in numbers:
        check_plates(plates, n)
