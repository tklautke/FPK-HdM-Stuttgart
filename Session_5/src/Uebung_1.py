"""
Übung aus einer Vorlesung des FPK. (Innerhalb der Vorlesung)
"""

teilnehmer = [["Theo", "Samara", "Michaeal"], ["Karsten", "Michel", "Santa"], ["Alice", "Peter", "Torben"]]

for gruppen_index in range(len(teilnehmer)):
    for teilnehmer_index in range(len(teilnehmer[gruppen_index])):
        print(f"Hallo mein Name ist {teilnehmer[gruppen_index][teilnehmer_index]} und ich bin in der Gruppe {gruppen_index + 1}")

print("done")