kunden = {1: 10000,2: 45,3: 96000}

for i in kunden:
    if kunden[i] > 1000:
        print(f'Kunden ID: {i} mit dem Kontostand {kunden[i]}')