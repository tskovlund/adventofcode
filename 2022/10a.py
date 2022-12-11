from readinput import readfile_and_split

cycle = 1
X = 1
sig_sum = 0
for instruction in readfile_and_split(" "):
    if cycle == 20 or (cycle - 20) % 40 == 0:
            sig_sum += cycle * X
    if instruction[0] == "noop":
        cycle += 1
    else:
        v = int(instruction[1])
        cycle += 1
        if cycle == 20 or (cycle - 20) % 40 == 0:
            sig_sum += cycle * X
        cycle += 1
        X += v
print(sig_sum)