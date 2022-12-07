from readinput import readfile_and_split

# 0: name
# 1: size
# 2: children
# 3: parent


def sum_dir_sizes_less_than(tree, n):
    if tree[2] is None:
        return 0
    s = tree[1] if tree[1] <= n else 0
    s += sum([sum_dir_sizes_less_than(node, n) for node in tree[2]])
    return s


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


print(sum_dir_sizes_less_than(current, 100000))
