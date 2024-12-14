robots = []
for line in open("Day14/input"):
    line = line.strip("\n").split(" ")
    left = line[0].strip("p=").split(",")
    right = line[1].strip("v=").split(",")
    robots.append({"x":int(left[0]), "y":int(left[1]), "vx":int(right[0]), "vy":int(right[1])})

# Part 1
def move_robot(r):
    r["x"] = (r["x"]+r["vx"]) % 101
    r["y"] = (r["y"]+r["vy"]) % 103

def find_quadrant(r, q):
    if r["x"] < 50 and r["y"] < 51: q[0] += 1
    elif r["x"] > 50 and r["y"] < 51: q[1] += 1
    elif r["x"] < 50 and r["y"] > 51: q[2] += 1
    elif r["x"] > 50 and r["y"] > 51: q[3] += 1
    return q

def show_symetrical_robots():
    screen = [["." for _ in range(101)] for _ in range(103)]
    for r in robots:
        screen[r["y"]][r["x"]] = "*"
    tree = False
    for line in screen:
        line = "".join(line)
        if "********" in line: tree = True
    if tree:
        for line in screen:
            print("".join(line))
    return tree

for second in range(100):
    for r in robots:
        move_robot(r)

quadrants = [0, 0, 0, 0]
for r in robots:
    quadrants = find_quadrant(r, quadrants)
print("Part one:", quadrants[0]*quadrants[1]*quadrants[2]*quadrants[3])


seconds = 100
while(True):
    seconds += 1
    for r in robots:
        move_robot(r)
    if show_symetrical_robots():
        print("Found in", seconds, "seconds.")
        input("\nContinue ?")
    if seconds%1000 == 0:
        print(seconds)