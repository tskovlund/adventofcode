from readinput import readfile

if __name__ == "__main__":
    print(sum(sorted([sum([int(e[:-1]) for e in g.split(":")]) for g in ":".join(readfile()).split(":\n:")])[-3:]))
