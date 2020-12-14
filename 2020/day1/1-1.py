#!/usr/bin/env python3
import itertools

line_list = []
target = 2020
with open("input.txt","r",) as file:
    for line in file:
        line_list.append(int(line.split("\n")[0]))


for numbers in itertools.combinations(line_list,2):
    if sum(numbers) == target:
        print("%s" %(numbers,) + "\n")
        print(numbers[0] * numbers[1])
