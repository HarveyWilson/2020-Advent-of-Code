with open('Day 3\\input.txt') as f:
    data = f.readlines()

column = 0
count = 0
for row in data:
    if row[column] == '#':
        count += 1
    column = (column + 3) % 31
print(count)
