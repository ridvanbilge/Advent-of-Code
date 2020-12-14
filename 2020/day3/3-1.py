#!/usr/bin/env python3

line_list = []
cursor = 0
trees = 0
with open("input.txt","r",) as file:
    for line in file:
        line_list.append(line.strip())

for i in range(len(line_list) - 1):
    line = line_list[i]
    line_length = len(line)
    cursor += 3
    cursor %= line_length
    if line_list[i + 1][cursor] == "#":
        trees += 1

print(trees)