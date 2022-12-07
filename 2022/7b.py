from readinput import readfile_and_split

# 0: name
# 1: size
# 2: children
# 3: parent

TOTAL = 70000000
NEED = 30000000


def find_smallest_dir_greater_than(tree, n, max):
    if tree[2] is None:
        return max
    s = tree[1]
    if s < n:
        s = max
    return min([s] + [find_smallest_dir_greater_than(child, n, max) for child in tree[2]])


filesystem = None
current = None
for line in readfile_and_split():
    if line[0].startswith("$"):
        cmd = line[1:]
        if cmd[0] == "cd":
            if cmd[1] == "..":
                current = current[3]
            else:
                if current:
                    new = [cmd[1], 0, [], current]
                    current[2].append(new)
                    current = new
                else:
                    filesystem = [cmd[1], 0, [], None]
                    current = filesystem
        if cmd[0] == "ls":
            continue
    else:
        if line[0].startswith("dir"):
            continue
        size = int(line[0])
        name = line[1]
        new = [name, size, None, current]
        current[2].append(new)
        parent = new[3]
        while parent:
            parent[1] += int(line[0])
            parent = parent[3]


# find root
while current[3]:
    current = current[3]

available = TOTAL - current[1]
need = NEED - available

print(find_smallest_dir_greater_than(current, need, TOTAL))
