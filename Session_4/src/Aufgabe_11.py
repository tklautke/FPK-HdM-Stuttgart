liste = [78,12,85,39,39,25,93,25,10,18]
groesste_zahl = 0
kleinste_zahl = 0

for index in range(len(liste)):

    if liste[index] -1 == -1: break

    if liste[index] > liste[index - 1]:
        groesste_zahl = liste[index]

    if liste[index] < liste[index - 1]:
        kleinste_zahl = liste[index]


print(groesste_zahl)
print(kleinste_zahl)