cw = []
for line in open("Day4/input"):
    cw.append(line.strip("\n"))

# Part 1

def check_xmas(i, j):
    res = 0
    if i <= len(cw)-4 and cw[i+1][j] == "M" and cw[i+2][j] == "A" and cw[i+3][j] == "S": res += 1
    if i >= 3 and cw[i-1][j] == "M" and cw[i-2][j] == "A" and cw[i-3][j] == "S": res += 1
    if j <= len(cw[0])-4 and cw[i][j+1] == "M" and cw[i][j+2] == "A" and cw[i][j+3] == "S": res += 1
    if j >= 3 and cw[i][j-1] == "M" and cw[i][j-2] == "A" and cw[i][j-3] == "S": res += 1

    if i <= len(cw)-4 and j <= len(cw[0])-4 and cw[i+1][j+1] == "M" and cw[i+2][j+2] == "A" and cw[i+3][j+3] == "S": res += 1
    if i <= len(cw)-4 and j >= 3 and cw[i+1][j-1] == "M" and cw[i+2][j-2] == "A" and cw[i+3][j-3] == "S": res += 1
    if i >= 3 and j <= len(cw[0])-4 and cw[i-1][j+1] == "M" and cw[i-2][j+2] == "A" and cw[i-3][j+3] == "S": res += 1
    if i >= 3 and j >= 3 and cw[i-1][j-1] == "M" and cw[i-2][j-2] == "A" and cw[i-3][j-3] == "S": res += 1
    return res

# Part 2

def check_x_mas(i, j):
    if i > 0 and i < len(cw)-1 and j > 0 and j < len(cw[0])-1:
        top_left = cw[i-1][j-1]
        top_right = cw[i-1][j+1]
        bot_left = cw[i+1][j-1]
        bot_right = cw[i+1][j+1]
        if top_left == "M" and top_right == "M" and bot_right == "S" and bot_left == "S": return 1
        if top_left == "M" and top_right == "S" and bot_right == "S" and bot_left == "M": return 1
        if top_left == "S" and top_right == "S" and bot_right == "M" and bot_left == "M": return 1
        if top_left == "S" and top_right == "M" and bot_right == "M" and bot_left == "S": return 1
    return 0
    
somme_1 = 0
somme_2 = 0
for i in range(len(cw)):
    for j in range(len(cw[0])):
        if cw[i][j] == "X": somme_1 += check_xmas(i, j)
        elif cw[i][j] == "A": somme_2 += check_x_mas(i, j)

print("Le nombre de XMAS est de", somme_1, "et le nombre de X-MAS", somme_2)