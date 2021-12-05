freunde1 = {1: 'Malte', 2: 'Timo', 3: 'Flo', 4: 'Hans', 5: 'Tina'}
freunde2 = {1: 'Jörgen', 2: 'Malte', 3: 'Peter', 4: 'Flo', 5: 'Hanna'}

passende_freunde = []

for i in freunde1:
    if freunde1[i] in freunde2.values():
        passende_freunde.append(freunde1[i])

for i in range(len(passende_freunde)):
    print(passende_freunde[i], end=' ')