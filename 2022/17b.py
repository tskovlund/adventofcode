from readinput import readfile
from itertools import cycle

# A Tetris simulator with only horizontal movement and no rotation.

# This part works by implementing some (admittedly ugly) cycle detection
# and skipping a lot of simulation.
# Caution: don't try this ~~at home~~ on the sample input as this code does
# not detect any cycle for that input. It might not work for your input either.

# Number of rocks to simulate
STOP = 1000000000000

# If DEBUG is True the simulation steps in PRINT_STEPS are printed.
# This is too slow for 2022 steps.
DEBUG = False
PRINT_STEPS = {0, 42, 120}


def dprint(*args, **kwargs):
    if DEBUG:
        if kwargs["index"] in PRINT_STEPS:
            print(*args, **{k: v for k, v in kwargs.items() if k != "index"})


def dprint_chamber(chamber, I):
    if I in PRINT_STEPS:
        for layer in chamber:
            for cell in layer:
                if cell == 2:
                    c = "#"
                elif cell == 1:
                    c = "@"
                else:
                    c = "."
                dprint(c, end="", index=I)
            dprint(index=I)
        dprint(index=I)


# Width of the chamber
WIDTH = 7
# Vertical distance from current tower height where a rock spawns
HEIGHT = 3
# Horizontal offset from left where a rock spawns
OFFSET = 2
# Number of rock shapes
NUM_ROCKS = 5


def ROCKS(i):
    rocks = [
        [[1, 1, 1, 1]],
        [
            [0, 1, 0],
            [1, 1, 1],
            [0, 1, 0],
        ],
        [
            [0, 0, 1],
            [0, 0, 1],
            [1, 1, 1],
        ],
        [
            [1],
            [1],
            [1],
            [1],
        ],
        [
            [1, 1],
            [1, 1],
        ],
    ]
    return [[cell for cell in layer] for layer in rocks[i]]


def GAP():
    return [[0 for _ in range(WIDTH)] for _ in range(HEIGHT)]


def left(chamber, rock, i, j):
    if j == 0:
        return chamber, False
    # check if can move
    can_move = True
    for k, layer in enumerate(rock):
        first = layer.index(1)
        can_move = can_move and not chamber[i + k][j + first - 1]
    # if yes, then move
    if can_move:
        for k, layer in enumerate(rock):
            for l, c in enumerate(layer):
                if c:
                    chamber[i + k][j + l - 1] = 1
                    chamber[i + k][j + l] = 0
    return chamber, can_move


def right(chamber, rock, i, j):
    width = len(rock[0])
    if j + width == WIDTH:
        return chamber, False
    # check if can move
    can_move = True
    for k, layer in enumerate(rock):
        last = width - 1 - layer[::-1].index(1)
        can_move = can_move and not chamber[i + k][j + last + 1]
    # if yes, then move
    if can_move:
        for k, layer in enumerate(rock):
            for l, c in enumerate(layer[::-1]):
                if c:
                    chamber[i + k][j + width - l] = 1
                    chamber[i + k][j + width - l - 1] = 0
    return chamber, can_move


def down(chamber, rock, i, j):
    height = len(rock)
    if i + height == len(chamber):
        return chamber, False
    can_move = True
    # check if can move
    for k, layer in enumerate(rock):
        for l, c in enumerate(layer):
            if c:
                if k < height - 1:
                    if not rock[k + 1][l]:
                        if chamber[i + k + 1][j + l]:
                            can_move = False
                else:
                    if chamber[i + k + 1][j + l]:
                        can_move = False
    # if yes, then move
    if can_move:
        for k, layer in enumerate(rock[::-1]):
            for l, c in enumerate(layer):
                if c:
                    chamber[i + height - k][j + l] = 1
                    chamber[i + height - k - 1][j + l] = 0
    return chamber, can_move


def fix_rock(chamber, rock, i, j):
    for k, layer in enumerate(rock):
        for l, c in enumerate(layer):
            if c == 1:
                chamber[i + k][j + l] = 2
    return chamber


def remove_empty_layers(chamber):
    i = 0
    while True:
        layer = chamber[i]
        try:
            layer.index(1)
            break
        except ValueError:
            try:
                layer.index(2)
                break
            except:
                i += 1
    return chamber[i:]


def remove_settled_layers(chamber, rock, i):
    height = len(rock)
    for k, layer in enumerate(chamber[i : i + height]):
        if layer.count(2) == len(layer):
            return chamber[: i + k], len(chamber) - (i + k)
    return chamber, 0


chamber = []
I = 0
next = True
removed_height = 0
potential_cycles = dict()
found_cycle = False
for k, c in enumerate(cycle(readfile()[0])):
    if not found_cycle:
        potential_cycle = (k % len(readfile()[0]), I % NUM_ROCKS, len(chamber))
        if potential_cycle in potential_cycles.keys():
            if chamber == potential_cycles[potential_cycle][0]:
                found_cycle = True
                old_I = potential_cycles[potential_cycle][1]
                delta_I = I - old_I
                old_height = potential_cycles[potential_cycle][2]
                delta_height = removed_height - old_height
                times = (STOP - I) // delta_I
                I += delta_I * times
                removed_height += delta_height * times
        potential_cycles[potential_cycle] = (
            [layer for layer in chamber],
            I,
            removed_height,
        )
    if I == STOP:
        break
    rock = ROCKS(I % NUM_ROCKS)
    if next:
        ROCK = [
            [0 for _ in range(OFFSET)]
            + layer
            + [0 for _ in range(WIDTH - 2 - len(rock[0]))]
            for layer in rock
        ]
        chamber = ROCK + GAP() + chamber
        dprint(f"Rock {I}", index=I)
        dprint_chamber(chamber, I)
        next = False
        i = 0
        j = 2
    if c == "<":
        dprint("<", index=I)
        chamber, moved = left(chamber, rock, i, j)
        if moved:
            j -= 1
    if c == ">":
        dprint(">", index=I)
        chamber, moved = right(chamber, rock, i, j)
        if moved:
            j += 1
    dprint_chamber(chamber, I)
    dprint("v", index=I)
    chamber, moved = down(chamber, rock, i, j)
    if not moved:
        next = True
        I += 1
        chamber = fix_rock(chamber, rock, i, j)
        dprint_chamber(chamber, I)
        chamber = remove_empty_layers(chamber)
        chamber, height = remove_settled_layers(chamber, rock, i)
        removed_height += height
    else:
        dprint_chamber(chamber, I)
        i += 1

print(len(chamber) + removed_height)
