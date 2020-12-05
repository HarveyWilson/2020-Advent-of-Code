import math


def calc_seat_position(seat):
    assert len(seat) is 10
    row = list(range(0, 128))
    for char in seat[:-3]:
        if char is 'F':
            row = row[:len(row)//2]
        elif char is 'B':
            row = row[math.ceil(len(row)/2):]

    column = list(range(0, 8))

    for char in seat[-3:]:
        if char is 'R':
            column = column[math.ceil(len(column)/2):]
        elif char is 'L':
            column = column[:len(column)//2]
    return row[0], column[0]


with open('Day 5/input.txt') as f:
    data = f.readlines()

data = [d.strip() for d in data]
seat_ids = []

for seat in data:
    seat_rc = calc_seat_position(seat)
    seat_ids.append(seat_rc[0]*8+seat_rc[1])

all_seats = list(range(min(seat_ids), max(seat_ids)+1))
empty_seat = set(seat_ids) ^ set(all_seats)
print(f'Puzzle 1: {max(seat_ids)}\nPuzzle 2:{empty_seat}')
