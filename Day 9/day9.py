with open('Day 9\\input.txt') as f:
    data = []
    for line in f.readlines():
        data.append(int(line.strip()))

for i in range(0,len(data)-25):
    window = data[i:i+25]
    values = window.copy()
    results = []
    result = data[i+25]
    for value in window:
        results.extend([x + value for x in values])
    if result not in results:
        print(result)
