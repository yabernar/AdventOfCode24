import copy as cp

data = ""
for line in open("Day9/input"):
    data = line.strip("\n")

#data = "14113"

array = []
file_id = 0
is_file = True
for character in data:
    if is_file:
        for _ in range(int(character)): array.append(file_id)
        file_id += 1
    else:
        for _ in range(int(character)): array.append(".")
    is_file = not is_file

array2 = cp.deepcopy(array)
#print(array2)

# Part 1
start = 0
end = len(array)-1
while start < end:
    if array[start] != ".": start += 1
    elif array[end] == ".": end -= 1
    else:
        array[start] = array[end]
        array[end] = "."

# Part 2
end = len(array2)-1
while end > 0:
    while array2[end] == ".": end -= 1
    size, file_id = 0, array2[end]
    while array2[end] == file_id: 
        size += 1
        end -= 1
    # search
    start, free_space = 0, 0
    while start <= end:
        if array2[start] != "." : free_space = 0
        else:
            free_space += 1
            if free_space >= size:
                for i in range(size):
                    array2[start-i] = file_id
                    array2[end+i+1] = "."
                #print(array2)
                start = end
        start += 1


def calculate_checksum(arr):
    checksum = 0
    for i in range(len(arr)):
        if arr[i] != ".": checksum += i*arr[i]
    return checksum

print("Part one :", calculate_checksum(array))
print("Part two :", calculate_checksum(array2))