def addieren(*args):
    ergebnis = args[0]
    for i in args[1:]:
        ergebnis = ergebnis + i

    return ergebnis


def subtrahieren(*args):
    ergebnis = args[0]
    for i in args[1:]:
        ergebnis = ergebnis - i

    return ergebnis


def multiplizieren(*args):
    ergebnis = args[0]
    for i in args[1:]:
        ergebnis = ergebnis * i

    return ergebnis


def dividieren(*args):
    ergebnis = args[0]
    for i in args[1:]:
        ergebnis = ergebnis / i

    return ergebnis


print(addieren(10, 5, 2, 4))
print(subtrahieren(10, 5, 1, 3)) #TODO beheben
print(multiplizieren(10, 5, 2, 1)) #TODO beheben
print(dividieren(10, 5, 0.5))
