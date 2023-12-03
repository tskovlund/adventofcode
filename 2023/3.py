from collections import defaultdict

from readinput import readfile


potential_gears_dict = defaultdict(lambda: [])


def update_potential_gears(potential_gears, number):
    for potential_gear in potential_gears:
        potential_gears_dict[potential_gear].append(number)


def is_symbol(char: str):
    return not char.isnumeric() and not char == "."


def is_asterisk(char: str):
    return char == "*"


def check_character(schematic, row, col):
    potential_gears = set()
    res = False
    max_col = len(schematic[row]) - 1
    max_row = len(schematic) - 1
    if row > 0:
        if col > 0:
            if is_symbol(schematic[row - 1][col - 1]):
                res = True
            if is_asterisk(schematic[row - 1][col - 1]):
                potential_gears.add((row - 1, col - 1))
        if is_symbol(schematic[row - 1][col]):
            res = True
        if is_asterisk(schematic[row - 1][col]):
            potential_gears.add((row - 1, col))
        if col < max_col:
            if is_symbol(schematic[row - 1][col + 1]):
                res = True
            if is_asterisk(schematic[row - 1][col + 1]):
                potential_gears.add((row - 1, col + 1))
    if col > 0:
        if is_symbol(schematic[row][col - 1]):
            res = True
        if is_asterisk(schematic[row][col - 1]):
            potential_gears.add((row, col - 1))
    if col < max_col:
        if is_symbol(schematic[row][col + 1]):
            res = True
        if is_asterisk(schematic[row][col + 1]):
            potential_gears.add((row, col + 1))
    if row < max_row:
        if col > 0:
            if is_symbol(schematic[row + 1][col - 1]):
                res = True
            if is_asterisk(schematic[row + 1][col - 1]):
                potential_gears.add((row + 1, col - 1))
        if is_symbol(schematic[row + 1][col]):
            res = True
        if is_asterisk(schematic[row + 1][col]):
            potential_gears.add((row + 1, col))
        if col < max_col:
            if is_symbol(schematic[row + 1][col + 1]):
                res = True
            if is_asterisk(schematic[row + 1][col + 1]):
                potential_gears.add((row + 1, col + 1))

    return res, potential_gears


def is_part_number(schematic, row, col):
    res = False
    number = ""
    potential_gears = set()
    char: str = schematic[row][col]
    while char.isdecimal():
        number += char
        check, _potential_gears = check_character(schematic, row, col)
        potential_gears = potential_gears.union(_potential_gears)
        if res or check:
            res = True
        col += 1
        if col == len(schematic[row]):
            break
        char = schematic[row][col]

    number = int(number)
    update_potential_gears(potential_gears, number)
    return res, number


def check_line(schematic, row):
    part_numbers = []
    line = schematic[row]
    col = 0
    while col < len(line):
        char: str = line[col]
        if char.isdecimal():
            res, number = is_part_number(schematic, row, col)
            if res:
                part_numbers += [number]
            col += len(str(number)) - 1
        col += 1

    return part_numbers


schematic = readfile()

s = 0
for row in range(len(schematic)):
    s += sum(check_line(schematic, row))
print(s)

s = 0
for numbers in potential_gears_dict.values():
    if len(numbers) == 2:
        s += numbers[0] * numbers[1]
print(s)
