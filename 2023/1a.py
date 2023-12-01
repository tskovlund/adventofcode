from readinput import readfile


def map_non_decimal(c: str):
    return int(c) if c.isnumeric() else ""


def find_digits(line: str):
    return tuple(filter(lambda e: e != "", map(map_non_decimal, line)))


def combine_digits(digits: tuple):
    return digits[0] * 10 + digits[-1]


print(sum(map(combine_digits, map(find_digits, readfile()))))
