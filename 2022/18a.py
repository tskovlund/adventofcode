from readinput import readfile_and_split
from util import neighbors_3d

cubes = {(x, y, z) for x, y, z in [map(int, line) for line in readfile_and_split(",")]}
surface = 6 * len(cubes)
for x, y, z in cubes:
    for x_, y_, z_ in neighbors_3d(x, y, z):
        if (x_, y_, z_) in cubes:
            surface -= 1
print(surface)