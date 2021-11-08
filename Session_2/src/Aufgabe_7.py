zahl1 = int(input("Gebe bitte die erste Zahl ein: "))
zahl2 = int(input("Gebe bitte die zweite Zahl ein: "))

if zahl1 % zahl2 != 0:
    print(f"Die Division hat einen Rest. Der Rest beträgt {zahl1 % zahl2}")
else:
    print("Die Division hat keinen Rest :)")
