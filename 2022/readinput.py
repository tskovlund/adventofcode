import sys

def readfile():
    if len(sys.argv) < 2:
        print("You need to specify an input file.")
        sys.exit(1)
    with open(sys.argv[1]) as f:
        return f.readlines()
