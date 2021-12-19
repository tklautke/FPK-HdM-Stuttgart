class Person:

    def __init__(self, name, elternteil_1, elternteil_2):
        self.name = name
        self.elternteil_1 = elternteil_1
        self.elternteil_2 = elternteil_2

    def sag_hallo(self):
        print(self.name)
        print(self.elternteil_1.name)
        print(self.elternteil_2.name)
        print(f'Hallo mein Name ist {self.name}. Meine Eltern sind {self.elternteil_1.name} und {self.elternteil_2.name}.')
