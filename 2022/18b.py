from readinput import readfile_and_split
from util import neighbors_3d
from functools import cache


@cache
def find_path_to_boundary(cube, cubes, x_bounds, y_bounds, z_bounds):
    visited = set(cubes)
    queue = [] if cube in visited else [cube]
    while queue:
        x, y, z = queue.pop()
        visited.add((x, y, z))
        if x in set(x_bounds) or y in set(y_bounds) or z in set(z_bounds):
            return True
        queue = list((neighbors_3d(x, y, z) - visited) - set(queue)) + queue
    return False


cubes = frozenset(
    {(x, y, z) for x, y, z in [map(int, line) for line in readfile_and_split(",")]}
)
surface = 0
x_bounds = (
    min(map(lambda cube: cube[0], cubes)),
    max(map(lambda cube: cube[0], cubes)),
)
y_bounds = (
    min(map(lambda cube: cube[1], cubes)),
    max(map(lambda cube: cube[1], cubes)),
)
z_bounds = (
    min(map(lambda cube: cube[2], cubes)),
    max(map(lambda cube: cube[2], cubes)),
)
for x, y, z in cubes:
    for cube in neighbors_3d(x, y, z):
        if find_path_to_boundary(cube, cubes, x_bounds, y_bounds, z_bounds):
            surface += 1
print(surface)
