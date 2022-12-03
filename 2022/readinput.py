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
        return [line.rstrip("\n") for line in open_file()]
