from readinput import readfile


def find_index(stream, size):
    for i in range(len(stream) - size):
        if len(set(stream[i : i + size])) == size:
            return i + size


stream = readfile()[0]
print(find_index(stream, 4))
print(find_index(stream, 14))
