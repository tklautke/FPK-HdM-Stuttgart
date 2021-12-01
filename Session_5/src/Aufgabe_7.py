l2 = [[1, 2, 3, 4], [5, 6], [7, 8, 9]]

# Ohne range()
ergebnis_ohne_range = 0

for i in l2:
    for j in i:
        ergebnis_ohne_range += j

print(ergebnis_ohne_range)

# Mit range()
ergebnis_mit_range = 0

for i in range(len(l2)):
    for j in range(len(l2[i])):
        ergebnis_mit_range += l2[i][j]

print(ergebnis_mit_range)
