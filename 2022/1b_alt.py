from readinput import readfile_with_newlines

if __name__ == "__main__":
    print(sum(sorted([sum([int(e[:-1]) for e in g.split(":")]) for g in ":".join(readfile_with_newlines()).split(":\n:")])[-3:]))
