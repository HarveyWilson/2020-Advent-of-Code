from collections import Counter
from itertools import groupby

with open('Day 6\\input.txt') as f:
    data = f.readlines()

data = [data.strip() for data in data]

group_responses = [list(g) for k, g in groupby(data,key=bool) if k]

c = Counter()
num_yes = 0
for group in group_responses:
    group_size = len(group)
    c = Counter()
    responses = ''.join(group)
    for letter in responses:
        c.update(letter)
    c = Counter({k:c for k,c in c.items() if c>=group_size})
    num_yes += len(c.values())
print(num_yes)