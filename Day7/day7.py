lst = []
for line in open("Day7/input"):
    nbrs = line.strip("\n").split(" ")
    nbrs[0] = nbrs[0].strip(":")
    lst.append(list(map(int, nbrs)))

# Part 1
def is_valid_calibration(target, current, rest):
    if rest == []: return target == current
    if current > target: return False
    return is_valid_calibration(target, current*rest[0], rest[1:]) or is_valid_calibration(target, current+rest[0], rest[1:])

part1 = 0
for line in lst:
    if is_valid_calibration(line[0], line[1], line[2:]): part1 += line[0]
print("Part one :", part1)

# Part 2
def is_valid_calibration2(target, current, rest):
    if rest == []: return target == current
    if current > target: return False
    return is_valid_calibration2(target, current*rest[0], rest[1:]) or is_valid_calibration2(target, current+rest[0], rest[1:]) or is_valid_calibration2(target, int(str(current)+str(rest[0])), rest[1:])

part2 = 0
for line in lst:
    if is_valid_calibration2(line[0], line[1], line[2:]): part2 += line[0]
print("Part two :", part2)
