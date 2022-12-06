from readinput import readfile

stream = readfile()[0]

i = 0
while i < len(stream) - 4:
    if len(set(stream[i : i + 4])) == 4:
        print(i + 4)
        break
    i += 1
