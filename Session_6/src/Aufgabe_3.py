freunde = {1: 'Malte', 2: 'Timo', 3: 'Flo'}


def ausgabe():
    for i in freunde:
        print(freunde[i])


ausgabe()
print('-------------')

freunde[4] = 'Nils'

freunde[2] = 'Timo Troll'

ausgabe()
