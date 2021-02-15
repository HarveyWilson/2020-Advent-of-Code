with open('Day 1\\input.txt') as f:
    data = f.readlines()

data = list(map(int,data))

while len(data)>3:
    a = data.pop()
    for b in data:
        if a + b == 2020:
            print(f'Puzzle 1: {a}, {b}. Answer is {a*b}')
        for c in data:
            if a + b + c == 2020:
                print(f'Puzzle 2: {a}, {b}, {c}. Answer is {a*b*c}')
