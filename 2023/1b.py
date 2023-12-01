from readinput import readfile


spelled_out_digits = {
    "one": "o1e",
    "two": "t2o",
    "three": "t3e",
    "four": "4",
    "five": "5e",
    "six": "6",
    "seven": "7n",
    "eight": "e8t",
    "nine": "n9e",
}


def map_spelled_out_digits(line: str):
    for key in spelled_out_digits.keys():
        line = line.replace(key, spelled_out_digits[key])
    return line


def map_non_decimal(c: str):
    return int(c) if c.isnumeric() else ""


def find_digits(line: str):
    return tuple(filter(lambda e: e != "", map(map_non_decimal, line)))


def combine_digits(digits: tuple):
    return digits[0] * 10 + digits[-1]


print(
    sum(map(combine_digits, map(find_digits, map(map_spelled_out_digits, readfile()))))
)
