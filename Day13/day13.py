arcades, machine = [], {}
for line in open("Day13/input"):
    if line == "\n": 
        arcades.append(machine)
        machine = {}
    elif "Button A:" in line: 
        machine["Ax"] = int(line[12:14])
        machine["Ay"] = int(line[18:20])
    elif "Button B:" in line: 
        machine["Bx"] = int(line[12:14])
        machine["By"] = int(line[18:20])
    elif "Prize:" in line:
        line = line.strip("\n").split(" ")
        machine["Tx"] = int(line[1].strip("X=,"))
        machine["Ty"] = int(line[2].strip("Y="))

# Part 1
def solve_machine(machine):
    nbr_B = (machine["Ty"] * machine["Ax"] - machine["Tx"] * machine["Ay"]) / (machine["Ax"] * machine["By"] - machine["Ay"] * machine["Bx"])
    nbr_A = (machine["Tx"] - machine["Bx"] * nbr_B) / machine["Ax"]
    if nbr_A % 1 == 0 and nbr_B % 1 == 0: return int(nbr_A*3+nbr_B)
    return 0

# Part 2
def solve_machine_corrected(machine):
    machine["Tx"] += 10000000000000
    machine["Ty"] += 10000000000000
    return solve_machine(machine)

tokens, tokens2 = 0, 0
for m in arcades:
    tokens += solve_machine(m)
    tokens2 += solve_machine_corrected(m)
print("Part one:", tokens)
print("Part two:", tokens2)