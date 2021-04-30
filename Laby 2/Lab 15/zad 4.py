import random

karty = ['2','3','4','5','6','7','8','9','10','W','D','K','A']

class Talia:
    talia = []
    stol = []

    def utworz_talie(self):
        for x in karty:
            self.talia.append(Karta('Karo',x))
        for x in karty:
            self.talia.append(Karta('Kier',x))
        for x in karty:
            self.talia.append(Karta('Pik',x))
        for x in karty:
            self.talia.append(Karta('Trefl',x))

    def porownaj(self):
        c1 = 0
        c2 = 0
        k1 = random.choice(self.talia)
        k2 = random.choice(self.talia)
        fig1 = k1.figura
        fig2 = k2.figura

        for x in karty:
            c1 += 1
            if x == fig1:
                break

        for z in karty:
            c2 += 1
            if z == fig2:
                break
        if c1 > c2:
            print('Karta {} jest wieksza od Karty {} '.format(k1,k2))
        elif c1 < c2:
            print('Karta {} jest mniejsza od karty {}'.format(k1,k2))
        else:
            print('Karty sa takie same')

    def sortuj(self):
        print(sorted(self.talia, key=lambda Karta:Karta.kolor))

        print(sorted(self.talia, key=lambda Karta:Karta.figura))

    def wyswietl(self,kolor,figura):
        for x in self.talia:
            if x.kolor == kolor and x.figura == figura:
                print('Karta {} {} jest w talii'.format(x.kolor,x.figura))

    def dodaj(self,kolor,figura):
        for x in self.talia:
            if x.kolor == kolor and x.figura == figura:
                print('Karta jest juz w talii')
            else:
                self.talia.append(Karta(kolor,figura))

    def usun(self,kolor,figura):
        for x in self.talia:
            if x.kolor == kolor and x.figura == figura:
                z = self.talia.index(x)
                self.talia.pop(z)

    def przenies(self,kolor,figura):
        for x in self.talia:
            if x.kolor == kolor and x.figura == figura:
                print("Karta zostala przeniesiona na stol")
                self.usun(kolor,figura)
                self.stol.append(Karta(kolor, figura))



class Karta:
    def __init__(self,kolor,figura):
        self.kolor = kolor
        self.figura = figura

    def __repr__(self):
        return "{} {}".format(self.kolor,self.figura)


talia = Talia()
talia.utworz_talie()
talia.porownaj()