#!/usr/bin/env python3
line_list = []
valid_passports = 0
attributes = ["ecl", "pid", "byr", "iyr", "eyr", "hgt", "hcl"]
new = ""
with open("input.txt","r",) as file:
    exampleText = file.read()
new = ""

for line in exampleText.split('\n'):
    if line == '':
        new += '\n\n'
    elif len(line) > 0:
        new += line + ' ' 
    else:
        new += line + '\n'
line_list = new.split("\n\n")
for i in range(len(line_list)):
    for attribute in attributes:
        if str(line_list[i]).find(attribute) == -1:
            break
    else:
        valid_passports += 1

print(valid_passports)