from readinput import readfile

sum = 0
for line in readfile():
    a, b = [list(map(int, i.split("-"))) for i in line.split(",")]
    if a[0] <= b[0] and a[1] >= b[1] or b[0] <= a[0] and b[1] >= a[1]:
        sum += 1
print(sum)
