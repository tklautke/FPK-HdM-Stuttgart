l1 = [[1, 2, 3, 4], [5, 6], [7, 8, 9]]

for i in range(len(l1)):
    innere_liste = l1[i]
    for j in range(len(innere_liste)):
         print(innere_liste[j], end=" ")
    print("\n")