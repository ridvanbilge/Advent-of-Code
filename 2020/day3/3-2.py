#!/usr/bin/env python3

line_list = []
combinations = [(1,1),(3,1),(5,1),(7,1),(1,2)]
result = 1

with open("input.txt","r",) as file:
    for line in file:
        line_list.append(line.strip())

for i,j in combinations:
    cursor = 0
    trees = 0
    for k in range(0,len(line_list) - j,j):
        line = line_list[k]
        line_length = len(line)
        cursor += i
        cursor %= line_length
        k += j
        if line_list[k][cursor] == "#":
            trees += 1
    result *= trees

print(result)
