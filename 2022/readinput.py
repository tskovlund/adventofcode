import sys


def open_file():
    if len(sys.argv) < 2:
        print("You need to specify an input file.")
        sys.exit(1)
    return open(sys.argv[1])


def readfile_with_newlines():
    with open_file() as f:
        return f.readlines()


def readfile():
    with open_file() as f:
        return [line.rstrip("\n") for line in f]


def readfile_and_split(s=" "):
    return [line.split(s) for line in readfile()]


def readgrid():
    return [list(map(int, line)) for line in readfile()]