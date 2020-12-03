from functools import reduce

def get_trees(slope, movement):
    column = 0
    count = 0
    length = len(slope[0])-1
    for i in range(0,len(data),movement[1]):
        if slope[i][column] =='#':
            count +=1
        column = (column + movement[0]) % length
    return count

with open('Day 3\\input.txt') as f:
    data = f.readlines()

slopes = [(1,1),(3,1),(5,1),(7,1),(1,2)]
ans = []
for slope in slopes:
    ans.append(get_trees(data,slope))

print(reduce((lambda x,y: x*y),ans))