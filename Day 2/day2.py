
def parse_range(q):
    a,b = q.split('-')
    return (int(a),int(b))

def valid_pass(positions, password, letter):    
    return (password[positions[0]-1] == letter) != (password[positions[1]-1] == letter)
    

with open('Day 2\\input.txt') as f:
    data = f.readlines()

#{range, letter, password}
data = [i.strip('\n').split(',') for i in data]

data = [password for q,letter,password in data if valid_pass(parse_range(q),password,letter)]

# data = [password for q,letter,password in data if password.count(letter) in parse_range(q)]

print(len(data))
