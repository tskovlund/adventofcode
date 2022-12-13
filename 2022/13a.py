from readinput import readfile_with_newlines


def compare(left, right):
    left = list(reversed(left))
    right = list(reversed(right))
    while left and right:
        l = left.pop()
        r = right.pop()
        if isinstance(l, int):
            if isinstance(r, int):
                if l < r:
                    return -1
                if r < l:
                    return 1
            else:
                left.append([l])
                right.append(r)
        elif isinstance(r, int):
            right.append([r])
            left.append(l)
        else:
            c = compare(l, r)
            if c != 0:
                return c
    if left and not right:
        return 1
    if right and not left:
        return -1
    return 0


index_sum = 0
for i, pair in enumerate("".join(readfile_with_newlines()).split("\n\n"), 1):
    left, right = [eval(line) for line in pair.rstrip("\n").split("\n")]
    if compare(left, right) == -1:
        index_sum += i
print(index_sum)
