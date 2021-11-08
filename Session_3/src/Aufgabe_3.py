startkapital = int(input("Geben sie ein Startkapital ein: "))
prozentsatz = float(input("Geben sie ein Prozentsatz ein: "))
zielkapital = int(input("Geben sie ein Zielkapital ein: "))

neuesErgebnis = startkapital

jahre = 0

while neuesErgebnis < zielkapital:
    neuesErgebnis = neuesErgebnis + (neuesErgebnis * prozentsatz)
    jahre += 1

print(f"Es braucht {jahre} Jahre")
