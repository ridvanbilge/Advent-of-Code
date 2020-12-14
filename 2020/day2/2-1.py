#!/usr/bin/env python3

line_list = []

with open("input.txt","r",) as file:
    for line in file:
        line_list.append(line.split())


count = 0
valid_list = []
for i in line_list:
    char_range = range(int(i[0].split("-")[0]), int(i[0].split("-")[1]))
    key_char = i[1][0]
    valid_list = [char_range, key_char, i[2]]
    if valid_list[2].count(valid_list[1]) in valid_list[0] or valid_list[2].count(valid_list[1]) == (valid_list[0][-1] + 1):
        count += 1

print(count)
