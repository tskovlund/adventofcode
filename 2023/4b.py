from collections import defaultdict

from readinput import readfile_and_split

copies = defaultdict(lambda: 1)

for i, (card, numbers) in enumerate(readfile_and_split(" | ")):
    copies[i] = copies[i]
    winning_numbers = set(card.split()[2:])
    numbers = set(numbers.split())
    matches = len(winning_numbers.intersection(numbers))
    for j in range(i + 1, i + 1 + matches):
        copies[j] += copies[i]

print(sum(copies.values()))
