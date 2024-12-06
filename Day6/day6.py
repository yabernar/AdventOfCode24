from sortedcontainers import SortedList

lst = []
for line in open("Day6/input"):
    lst.append(list(line.strip("\n")))

# Find the guard
guard_x, guard_y = 0, 0
for i in range(len(lst)):
    if "^" in lst[i]: 
        guard_x, guard_y = i, lst[i].index("^")
        break
lst[guard_x][guard_y] = "X"

# Count Xs
def count_Xs():
    total = 0
    for line in lst:
        total += line.count("X")
    return total

# Part 1
def turn_right(direction):
    if direction == "Up": return "Right"
    if direction == "Right": return "Down"
    if direction == "Down": return "Left"
    if direction == "Left": return "Up"

def avancer(x, y, direction):
    while True:
        lst[x][y] = "X"
        if direction == "Up": new = (x-1, y)
        elif direction == "Right": new = (x, y+1)
        elif direction == "Down": new = (x+1, y)
        elif direction == "Left": new = (x, y-1)
    
        if new[0] < 0 or new[0] >= len(lst) or new[1] < 0 or new[1] >= len(lst[0]): return lst
        elif lst[new[0]][new[1]] == "#": direction = turn_right(direction)
        else: x, y = new[0], new[1]

# Part 2
def to_string(x, y, direction):
    return str(x)+","+str(y)+","+direction

def check_loop(x, y, direction, block_x, block_y):
    visited = SortedList()
    while True:
        current = to_string(x,y,direction)
        if current in visited: return 1
        else: visited.add(current)

        if direction == "Up": new = (x-1, y)
        elif direction == "Right": new = (x, y+1)
        elif direction == "Down": new = (x+1, y)
        elif direction == "Left": new = (x, y-1)
    
        if new[0] < 0 or new[0] >= len(lst) or new[1] < 0 or new[1] >= len(lst[0]): return 0
        elif lst[new[0]][new[1]] == "#" or (new[0]==block_x and new[1]==block_y): direction = turn_right(direction)
        else: x, y = new[0], new[1]

# Prints
avancer(guard_x, guard_y, "Up")
print("Part one :", count_Xs())

res = 0
for i in range(len(lst)):
    for j in range(len(lst[0])):
        if lst[i][j] == "X" and not (i == guard_x and j == guard_y):
            res += check_loop(guard_x, guard_y, "Up", i, j)
print("Part two:", res)