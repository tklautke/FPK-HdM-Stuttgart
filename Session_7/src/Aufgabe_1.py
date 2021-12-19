file = open('Einkaufsliste.txt', 'r')

einkaufsliste_liste = []

for item in file:
    short_item = item[:-1]
    einkaufsliste_liste.append(short_item)

file.close()

einkaufsliste_liste.sort()

print(einkaufsliste_liste)


new_file = open('Sotierte_Einkaufsliste.txt', 'a')

for item in einkaufsliste_liste:
    new_file.write(item + '\n')

new_file.close()