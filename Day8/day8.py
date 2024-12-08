lst = []
for line in open("Day8/input"):
    lst.append(line.strip("\n"))

# Part 1 & 2
antinodes = [[0 for _ in range(len(lst[0]))] for _ in range(len(lst))]
antinodes_rh = [[0 for _ in range(len(lst[0]))] for _ in range(len(lst))]

def propagate(x, y, dx, dy):
    antinode_x = x + dx
    antinode_y = y + dy
    if antinode_x >= 0 and antinode_x < len(lst) and antinode_y >= 0 and antinode_y < len(lst[0]): 
        antinodes_rh[antinode_x][antinode_y] = 1
        propagate(antinode_x, antinode_y, dx, dy)


def find_antinodes(x, y, resonant_harmonics):
    antenna_type = lst[x][y]
    for i in range(len(lst)):
        for j in range(0, len(lst[0])):
            if lst[i][j] == antenna_type and i != x and j != y:
                if resonant_harmonics:
                    dx, dy = (i-x), (j-y)
                    propagate(x, y, dx, dy)
                    propagate(x, y, -dx, -dy)
                else: 
                    antinode_x = x - (i - x)
                    antinode_y = y - (j - y)
                    if antinode_x >= 0 and antinode_x < len(lst) and antinode_y >= 0 and antinode_y < len(lst[0]): 
                        antinodes[antinode_x][antinode_y] = 1

for i in range(len(lst)):
    for j in range(0, len(lst[0])):
        if lst[i][j] != ".": 
            find_antinodes(i, j, False)
            find_antinodes(i, j, True)
print("Part one :", sum(sum(row) for row in antinodes))
print("Part two :", sum(sum(row) for row in antinodes_rh))