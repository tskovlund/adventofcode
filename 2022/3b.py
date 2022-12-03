from readinput import readfile

lines = readfile()
i = 0
sum = 0
while i < len(lines):
    common = set(lines[i]).intersection(set(lines[i + 1])).intersection(set(lines[i + 2]))
    for c in common:
        if ord(c) >= 97:
            sum += ord(c) - 96
        else:
            sum += ord(c) - 65 + 27
    i += 3
print(sum)