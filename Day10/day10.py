topo_map = []
for line in open("Day10/input"):
    topo_map.append(line.strip("\n"))

# Part 1
def follow_path(x, y, altitude):
    if altitude == 9: return [(x,y)] # Creates a one pair set
    reachable_summits = []
    if x > 0 and topo_map[x-1][y] == str(altitude+1): reachable_summits.extend(follow_path(x-1, y, altitude+1))
    if x < len(topo_map)-1 and topo_map[x+1][y] == str(altitude+1): reachable_summits.extend(follow_path(x+1, y, altitude+1))
    if y > 0 and topo_map[x][y-1] == str(altitude+1): reachable_summits.extend(follow_path(x, y-1, altitude+1))
    if y < len(topo_map[0])-1 and topo_map[x][y+1] == str(altitude+1): reachable_summits.extend(follow_path(x, y+1, altitude+1))
    return reachable_summits

def explore_trailhead(x, y):
    summits = follow_path(x, y, 0)
    return len(set(summits)), len(summits)

total_score, total_rating = 0, 0
for i in range(len(topo_map)):
    for j in range(len(topo_map[0])):
        if topo_map[i][j] == "0":
            res = explore_trailhead(i, j)
            total_score += res[0]
            total_rating += res[1]
    
print("Part one :", total_score)
print("Part two :", total_rating)