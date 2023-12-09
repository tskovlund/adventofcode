from readinput import readfile_and_split

s = 0
for card, numbers in readfile_and_split(" | "):
    winning_numbers = set(card.split()[2:])
    numbers = set(numbers.split())
    s += 2 ** (len(winning_numbers.intersection(numbers)) - 1) // 1
print(int(s))
