from readinput import readfile

stream = readfile()[0]

i = 0
while i < len(stream) - 14:
    if len(set(stream[i : i + 14])) == 14:
        print(i + 14)
        break
    i += 1
