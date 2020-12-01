with open('Day1\\input.txt') as f:
    data = f.readlines()

data = list(map(int,data))

while len(data)>3:
    a = data.pop()
    for b in data:
        for c in data:
            if a + b + c == 2020:
                print(a,b,c)
