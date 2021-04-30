import random

class Hotel:
    def __init__(self, pietra, liczba_pokoi,):
        self.pietra = pietra
        self.liczba_pokoi = liczba_pokoi
        self.liczba_pieter = []
        self.pokoje = []



        for x in range(self.pietra):
            self.liczba_pieter.append([])

        self.utworz()

    def utworz(self):
        # print(self.liczba_pieter)
        u = 0
        for y in range(self.pietra):
            j =  random.randint(1,self.liczba_pokoi - u)
            # liczba_pok_piet = random.randint(1, self.liczba_pokoi - self.pietra)
            u += j
            for x in range(j):
                self.liczba_pieter[y].append(x)
                self.pokoje.append(x)




    def wolne_pok(self):
        counter = 0
        for x in self.pokoje:
            if x.zajety == False:
                counter += 1
        print('Jest {} wolnych pokoi'.format(counter))

    def wynajecie(self,osoba):
        for x in self.pokoje:
            if x.zajety == False:
                x.zajety = True
                x.lokator = osoba #zamiast osoba to Osoba(osoba.imie)

    def znajdz(self,osoba):
        for x in self.pokoje:
            if x.lokator.imie == osoba.imie:
                print('Osoba {} wynajmuje pokoj'.format(osoba))

class Pokoj:
    def __init__(self,nr,pietro):
        self.nr = nr
        self.pietro = pietro
        self.zajety = False
        self.lokator = None

    def __repr__(self):
        return 'Pokoj {} znajduje sie na pietrze {}'.format(self.nr,self.pietro)

class Osoba:
    def __init__(self, imie):
        self.imie = imie

    def __repr__(self):
        return '{}'.format(self.imie)








h1 = Hotel(4,14)
# h1.utworz()
print(h1.liczba_pieter)