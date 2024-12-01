f = open("Day1/input", 'r')
gauche = []
droite = []
for line in f:
    word = line.rstrip("\n").split("   ")
    gauche.append(int(word[0]))
    droite.append(int(word[1]))
f.close()

# Part 1
gauche.sort()
droite.sort()
somme = 0
for i in range(len(gauche)):
    somme += abs(gauche[i] - droite[i])
print("La distance entre les listes est de", somme)

# Part 2
somme = 0
for nbr in gauche:
    somme += nbr * droite.count(nbr)
print("La similarité entre les listes est de", somme)
