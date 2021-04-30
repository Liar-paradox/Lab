import random

class Hotel:
    def __init__(self, pietra, liczba_pokoi,):
        self.pietra = pietra
        self.liczba_pokoi = liczba_pokoi
        self.liczba_pieter = []



        for x in range(self.pietra):
            self.liczba_pieter.append([])


    def utworz(self):
        print(self.liczba_pieter)
        for y in range(self.pietra):
            liczba_pok_piet = random.randint(1, self.liczba_pokoi - self.pietra)
            for x in range(liczba_pok_piet):
                self.liczba_pieter[y].append(x)
        print(self.liczba_pieter)







h1 = Hotel(4,14)
h1.utworz()

