from readinput import readfile_and_split

cycle = 0
X = 1
instructions = readfile_and_split(" ")
n = sum([1 if i[0] == "noop" else 2 for i in instructions])
print(n)
pixels = ["." for _ in range(n)]
for instruction in instructions:
    if abs(X - cycle % 40) <= 1:
        pixels[cycle] = "#"
    if instruction[0] == "noop":
        cycle += 1
    else:
        v = int(instruction[1])
        cycle += 1
        if abs(X - cycle % 40) <= 1:
            pixels[cycle] = "#"
        cycle += 1
        X += v
for i in range(0, n, 40):
    print("".join(pixels[i : i + 40]))
