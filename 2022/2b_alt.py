from readinput import readfile

scores = [1, 2, 3]
opponent = {
    "A": 0,
    "B": 1,
    "C": 2,
}

score = 0
for r in readfile():
    o, y = r.split(" ")
    if y == "X": # lose
        score += scores[(opponent[o] - 1) % 3]
    if y == "Y": # draw
        score += scores[opponent[o]] + 3
    if y == "Z": # win
        score += scores[(opponent[o] + 1) % 3] + 6
print(score)
