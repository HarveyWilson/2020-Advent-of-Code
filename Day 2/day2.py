
def parse_range(q):
    a,b = q.split('-')
    return int(a),int(b)+1

def valid_pass(positions, password, letter):    
    return (password[positions[0]-1] == letter) != (password[positions[1]-2] == letter)
    

with open('Day 2\\input.txt') as f:
    data = f.readlines()

#{range, letter, password}
data = [i.strip('\n').split(',') for i in data]

puzzle2 = [password for q,letter,password in data if valid_pass(parse_range(q),password,letter)]

puzzle1 = [password for q,letter,password in data if password.count(letter) in range(*parse_range(q))]

print(f'Puzzle 1: {len(puzzle1)}\nPuzzle 2: {len(puzzle2)}')
