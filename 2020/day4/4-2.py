#!/usr/bin/env python3
import re
line_list = []
valid_list = []
attributes = ["ecl", "pid", "byr", "iyr", "eyr", "hgt", "hcl"]
eye_colors = ['amb', 'blu', 'brn', 'gry', 'grn', 'hzl', 'oth']
count = 0
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
        valid_list.append(line_list[i])         

valid_dict = {}
second_list = []

for i in valid_list:
    a = dict([item.split(':') for item in i.split()])
    second_list.append(a)

for i in second_list:
    if 1920 <= int(i["byr"]) <= 2002:
        if 2010 <= int(i["iyr"]) <= 2020:
            if 2020 <= int(i["eyr"]) <= 2030:
                if ("cm" in i["hgt"] and 150 <= int(i["hgt"][:-2]) <= 193) or ("in" in i["hgt"] and 59 <= int(i["hgt"][:-2]) <= 76):
                    if i["hcl"].startswith("#") and re.match("^#([0-9a-zA-Z]{6,})", i["hcl"]):
                        for color in eye_colors:
                            if color == i["ecl"]:
                                if len(i["pid"]) == 9 and i["pid"].isnumeric():
                                    count += 1
print(count)
                                    