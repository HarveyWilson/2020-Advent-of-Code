from collections import Counter

with open('Day 10\\input.txt') as f:
    data = [int(d.strip()) for d in f.readlines()]

adapter_chain = [0]
valid_adapters = []
current_jolt = 0
i = 0
while i < len(data):
    j = i
    valid_adapters = []
    current_jolt = adapter_chain[len(adapter_chain)-1]
    while j < len(data):
        if data[j] - current_jolt in [0, 1, 2, 3]:
            valid_adapters.append(data[j])
        j += 1
    
    adapter_chain.append(min(valid_adapters))
    data.remove(min(valid_adapters))
    j += 1

last = adapter_chain[1]
counts = Counter([1,3])

for jolt in adapter_chain[2:]:
    counts[jolt-last] += 1
    last = jolt
print(counts)