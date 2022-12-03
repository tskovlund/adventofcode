from readinput import readfile

sum = 0
for contents in readfile():
    left = set(contents[:len(contents)//2])
    right = set(contents[len(contents)//2:])
    common = left.intersection(right)
    for c in common:
        if ord(c) >= 97:
            sum += ord(c) - 96
        else:
            sum += ord(c) - 65 + 27
print(sum)