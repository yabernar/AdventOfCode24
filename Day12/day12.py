garden = []
for line in open("Day12/input"):
    garden.append(line.strip("\n"))

# Part 1 & 2
visited = {}

def to_str(x, y):
    return str(x)+","+str(y)

def check_neighbor(visi, x, y, plant):
    if x >= 0 and x < len(garden) and y >= 0 and y < len(garden[0]) and garden[x][y] == plant:
        if to_str(x,y) not in visi: return explore_area(visi, x, y)
        else: return 0, 0, 0
    else: return 0, 1, 0

def check_corner(corner, side1, side2, opposite):
    if side1 != corner and side2 != corner: return 1
    if opposite == corner and ((side1 == corner and side2 != corner) or (side2 == corner and side1 != corner)): return 0.5
    return 0

def safe_access(x, y):
    if x >= 0 and x < len(garden) and y >= 0 and y < len(garden[0]): 
        return garden[x][y]
    return "Outside"

def check_all_corners(x, y, plant):
    top_left = check_corner(plant, safe_access(x-1, y), safe_access(x, y-1), safe_access(x-1, y-1))
    top_right = check_corner(plant, safe_access(x-1, y), safe_access(x, y+1), safe_access(x-1, y+1))
    bot_right = check_corner(plant, safe_access(x+1, y), safe_access(x, y+1), safe_access(x+1, y+1))
    bot_left = check_corner(plant, safe_access(x+1, y), safe_access(x, y-1), safe_access(x+1, y-1))
    return top_left + top_right + bot_right + bot_left

def explore_area(visi, x, y):
    visi[to_str(x,y)] = True
    plant = garden[x][y]
    a = check_neighbor(visi, x-1, y, plant)
    b = check_neighbor(visi, x+1, y, plant)
    c = check_neighbor(visi, x, y-1, plant)
    d = check_neighbor(visi, x, y+1, plant)
    area = 1 + a[0] + b[0] + c[0] + d[0]
    perimeter = a[1] + b[1] + c[1] + d[1]
    corners = check_all_corners(x,y,plant) + a[2] + b[2] + c[2] + d[2]
    return area, perimeter, corners

total_cost, reduced_cost = 0, 0
for i in range(len(garden)):
    for j in range(len(garden[0])):
        if to_str(i,j) not in visited:
            res = explore_area(visited, i, j)
            total_cost += res[0] * res[1]
            reduced_cost += res[0] * res[2]
print("Part one :", total_cost)
print("Part two :", int(reduced_cost))
