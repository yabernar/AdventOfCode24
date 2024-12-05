rules = {}
lst = []

for line in open("Day5/input"):
    line.strip("\n")
    if "|" in line:
        line = line.split("|")
        key, value = int(line[1]), int(line[0])
        if key in rules.keys():
            rules[key].append(value)
        else:
            rules[key] = [value]
    if "," in line:
        line = line.split(",")
        lst.append(list(map(int, line)))

# Part 1
def is_valid(previous, full, page):
    if page in rules.keys():
        for required in rules[page]:
            if required in full and required not in previous: return False
    return True

def check_order(line):
    current = []
    for page in line:
        if is_valid(current, line, page): current.append(page)
        else: return False
    return True

# Part 2
def reorder(line):
    new_line = []
    for i in range(len(line)):
        j = i
        while not is_valid(new_line, line, line[j]): j = j+1 
        new_line.append(line[j])
        tmp = line[j]
        line[j] = line[i]
        line[i] = tmp
    return new_line

# Both
part1, part2 = 0, 0
for line in lst:
    if check_order(line): part1 += line[len(line)//2]
    else : 
        line = reorder(line)
        part2 += line[len(line)//2]
print("Part 1:", part1, "Part 2:", part2)
