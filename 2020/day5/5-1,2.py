#!/usr/bin/env python3
seat_codes = []
seats = []

with open("input.txt","r",) as file:
    for line in file:
        seat_codes.append(line.strip())

for i in seat_codes:
    row = i[:7]
    column = i[7:]
    start = 0
    end = 127
    for char in row:
        if char == "F":
            end = int((start+end+1)/2) - 1
        elif char == "B":
            start = int((start+end+1)/2)
    seat_row = end
    start = 0
    end = 7
    for char in column:
        if char == "L":
            end = int((start+end+1)/2) - 1
        elif char == "R":
            start = int((start+end+1)/2)
    seat_column = end
    seat_id = (seat_row * 8) + seat_column
    seats.append(seat_id)

print(f"Solution of Puzzle 1: {max(seats)}")

# Solution 2
range_list = list(range(min(seats), max(seats)))
for i in seats:
    if i in range_list:
        range_list.remove(i)
print(f"Solution of Puzzle 2: {range_list[0]}")
