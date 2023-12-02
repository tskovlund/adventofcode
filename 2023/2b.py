from functools import reduce

from readinput import readfile_and_split


def compute_cube_power(game):
    limits = {
        "red": 0,
        "green": 0,
        "blue": 0,
    }

    for reveal in game:
        for kind in reveal.split(", "):
            amount, color = kind.split(" ")
            limits[color] = max(limits[color], int(amount))

    return reduce(lambda x, y: x * y, limits.values())


s = 0
for id, game in enumerate(readfile_and_split("; "), start=1):
    game[0] = game[0].split(": ")[1]
    s += compute_cube_power(game)

print(s)
