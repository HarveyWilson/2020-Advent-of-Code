import collections

with open('Day 6\\input.txt') as f:
    data = f.readlines()

data = [data.strip() for data in data]

c = collections.Counter()
num_yes = 0
for form in data:
    if not form:
        num_yes += len(c.values())
        c = collections.Counter()
    else:
        for letter in form:
            c.update(letter)

num_yes += len(c.values())
print(num_yes, len(c.values()))
