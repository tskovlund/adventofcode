from readinput import readfile

opponent = {
    "A": 1,
    "B": 2,
    "C": 3,
}

score = 0
for r in readfile():
    o, y = r[:-1].split(" ")
    if y == "X": # lose
        score += opponent[o] - 1
        if o == "A":
            score += 3
    if y == "Y": # draw
        score += opponent[o] + 3
    if y == "Z": # win
        score += opponent[o] + 1 + 6
        if o == "C":
            score -= 3
print(score)
