import sys
import os

filename = os.path.basename(__file__).split(".")[0][:-1] + ".txt"
if len(sys.argv) > 1:
    filename = sys.argv[1]

N = 80

def decrement(n):
    if n < 7:
        return n
    else:
        return n - 7

count = [0]*9

with open(filename) as f:
    line = map(int, f.readline().split(","))
    for i in line:
        count[i] += 1

    rest = N % 7

    for i in range(7, N, 7):
        new_count = [0]*9
        for j, c in enumerate(count):
            d = decrement(j)
            new_count[d] += c
            if j < 7:
                new_count[d + 2] += c
        count = new_count
    
    print(sum(count) + sum(count[:rest]))
