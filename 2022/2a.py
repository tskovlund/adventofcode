from readinput import readfile

opponent = {
    "A": 1,
    "B": 2,
    "C": 3,
}
you = {
    "X": 1,
    "Y": 2,
    "Z": 3,
}

score = 0
for r in readfile():
    o, y = r.split(" ")
    score += you[y]
    if opponent[o] == you[y]:
        score += 3
    if you[y] == (opponent[o] % 3) + 1:
        score += 6
print(score)
