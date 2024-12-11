for line in open("Day11/input"):
    stones = line.strip("\n").split(" ")
stones = list(map(int, stones))

stones_count = {}
for stone in stones:
    if stone not in stones_count: stones_count[stone] = 1
    else: stones_count[stone] += 1

# Part 1 & 2
def add_to_dic(dic, key, value):
    if key not in dic: dic[key] = value
    else: dic[key] += value
    return dic

def blink(stones):
    new_stones = {}
    if 0 in stones: new_stones[1] = stones.pop(0)
    for stone in stones:
        digits = str(stone)
        if len(digits)%2 == 0:
            part_length = len(digits)//2
            new_stones = add_to_dic(new_stones, int(digits[0:part_length]), stones[stone])
            new_stones = add_to_dic(new_stones, int(digits[part_length:]), stones[stone])
        else:
            new_stones = add_to_dic(new_stones, stone*2024, stones[stone])
    return new_stones

for i in range(25):
    stones_count = blink(stones_count)
print("Part one :", sum(stones_count.values()))
for i in range(50):
    stones_count = blink(stones_count)
print("Part two :", sum(stones_count.values()))