a = "rjgvinpzwtumc invuwpjtgzrmc tpuijngovwmrz mtcnwivgzrjup "

a = a[:-1]
b = list(a.split(" "))
sets = []


for i in b:
    sets.append(set(i))
print(len(sets[0].intersection(*sets[1:])))