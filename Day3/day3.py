import re

f = open("Day3/input", 'r')
lst = []
for line in f: lst.append(line)
f.close()

# Part 1
pattern = r"mul\([0-9]+,[0-9]+\)"

somme = 0
for line in lst:
    matches = re.findall(pattern, line)
    for match in matches:
        nbrs = match.strip("mul()").split(",")
        somme += int(nbrs[0]) * int(nbrs[1])
print("La somme des multiplications est de", somme)

# Part 2
pattern = r"mul\([0-9]+,[0-9]+\)|do\(\)|don\'t\(\)"

somme = 0
do = True
for line in lst:
    matches = re.findall(pattern, line)
    for match in matches:
        if match == "do()": do = True
        elif match == "don't()": do = False
        elif do:
            nbrs = match.strip("mul()").split(",")
            somme += int(nbrs[0]) * int(nbrs[1])
print("La somme des multiplications est de", somme)
