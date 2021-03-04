with open('Day 9\\input.txt') as f:
    data = []
    for line in f.readlines():
        data.append(int(line.strip()))

weakness = None
for i in range(0, len(data)-25):
    window = data[i:i+25]
    values = window.copy()
    results = []
    result = data[i+25]
    for value in window:
        results.extend([x + value for x in values])
    if result not in results:
        weakness = result
        break
print(weakness)

r = None
for i in range(len(data)-1):
    sum = 0
    j = i+1
    while sum < weakness:
        sum += data[j]
        j += 1
        if sum == weakness:
            r = (i, j)
            break
    if r is not None:
        break

print(min(data[r[0]:r[1]+1])+max(data[r[0]:r[1]+1]))
print(r)
