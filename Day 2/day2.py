
def parse_range(q):
    a,b = q.split('-')
    return range(int(a),int(b)+1)

with open('Day 2\\input.txt') as f:
    data = f.readlines()

#{range, letter, password}
data = [i.strip('\n').split(',') for i in data]

data = [password for q,letter,password in data if password.count(letter) in parse_range(q)]

print(len(data))
