eingabe = int(input("Gebe eine Primzahl ein: "))

for i in range(2, int(eingabe / 2) + 1):
    if (eingabe % i) == 0:
        print(f"{eingabe} ist keine Primzahl")
        break
else:
    print(f"{eingabe} ist eine Primzahl")
