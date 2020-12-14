#!/usr/bin/env python3
line_list = []

with open("input.txt","r",) as file:
    exampleText = file.read()

new = ""
count_sum1 = 0
count_sum2 = 0

for line in exampleText.split('\n'):
    if line == '':
        new += '\n\n'
    elif len(line) > 0:
        new += line + ' '
    
line_list = new.split("\n\n")

for i in line_list:
    i = i.replace(" ", "").lower()
    count = (len("".join(set(i))))
    count_sum1 += count

print(f"Solution of Puzzle 1: {count_sum1}")

# Solution 2
sets = []
for j in line_list:
    group = list(j.split(" "))
    for i in group:
        for k in i:
            sets.append(set(i))
    count = len(sets[0].intersection(*sets[1:]))
    count_sum2 += count
    sets = []

print(f"Solution of Puzzle 2: {count_sum2}")
