from readinput import readfile_and_split

limits = {
    "red": 12,
    "green": 13,
    "blue": 14,
}


def is_valid_game(game):
    for reveal in game:
        for kind in reveal.split(", "):
            amount, color = kind.split(" ")
            if int(amount) > limits[color]:
                return False
    return True


s = 0
for id, game in enumerate(readfile_and_split("; "), start=1):
    game[0] = game[0].split(": ")[1]
    if is_valid_game(game):
        s += id

print(s)
