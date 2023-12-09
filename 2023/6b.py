from readinput import readfile_and_split

lines = readfile_and_split(None)
time = int("".join(lines[0][1:]))
dist = int("".join(lines[1][1:]))

start = 0
while True:
    if start * (time - start) > dist:
        break
    start += 1

end = time
while True:
    if end * (time - end) > dist:
        break
    end -= 1

print(end - start + 1)
