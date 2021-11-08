print("Rechnung: Zahl1+Zahl2-Zahl3")

zahl1 = int(input("Gebe bitte die erste Zahl ein: "))
zahl2 = int(input("Gebe bitte die zweite Zahl ein: "))
zahl3 = int(input("Gebe bitte die dritte Zahl ein: "))

richtigeErgebnis = zahl1 + zahl2 - zahl3

print(richtigeErgebnis)

gussedErgebnis = int(input("Bitte tippe dein Ergbnis: "))

if gussedErgebnis == richtigeErgebnis:
    print("Dein Tipp war richtig :)")
elif gussedErgebnis != richtigeErgebnis:
    print(f"Dein Tipp war leider falsch :( Das richtige Ergbnis ist: {richtigeErgebnis}")
