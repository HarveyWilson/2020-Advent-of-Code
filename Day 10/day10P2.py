from collections import Counter

with open('Day 10\\input.txt') as f:
    data = [int(d.strip()) for d in f.readlines()]

data.append(0)
data.sort()
data.append(max(data)+3)
current_sum = []
valid_paths = [1]

for index, adapter in enumerate(data[1:]):
    i = index
    while adapter - data[i] in [0, 1, 2, 3]:
        current_sum.append(valid_paths[i])
        i -= 1
        if i==-1: break
    valid_paths.append(sum(current_sum))
    current_sum = []
    
print(max(valid_paths))