from random import randint

zaehler = 1

while randint(1, 6) != 6:
    print(f"Versuch {zaehler}")
    zaehler += 1

print(f"Es hat {zaehler} versuche gedauert :)")
