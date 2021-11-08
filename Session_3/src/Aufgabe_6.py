for i in range(3, 11):
    for j in range(2, int(i / 2) + 1):
        if (i % j) == 0:
            print(f"{i} ist keine Primzahl")
            break
    else:
        print(f"{i} ist eine Primzahl")
