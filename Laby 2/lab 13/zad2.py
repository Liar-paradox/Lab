ksiazki = []

class Ksiazka:
    def __init__(self,autor,tytul,kategoria,okladka,ilosc_str):
        self.autor = autor
        self.tytul = tytul
        self.kategoria = kategoria
        self.okladka = okladka
        self.ilosc_str = ilosc_str

    def __repr__(self):
        return 'ksiazka {} o tytule {} z kategori {} w {} okladce i {}'.format(self.autor, self.tytul, self.kategoria, self.okladka, self.ilosc_str)

    def znajdz(self):
        x = int(input('Podaj numer ksiazki: '))
        for x in ksiazki:
            print(x)

    def czytaj(self):
        return 'Czytasz w tym momencie ksiazke {} napisana przez {} '.format(self.tytul, self.autor)

    def oddaj(self):
        print('Oddajesz do biblioteki {} autorstwa {}'.format(self.tytul,self.autor))




for x in range(1):
    autor = str(input('Podaj autora: '))
    tytul = str(input('Podaj tytul: '))
    kategoria = str(input('Podaj kategorie: '))
    okladka = str(input('Jaka okladka: '))
    ilosc_str = int(input('Ile stron ma: '))
    k1 = Ksiazka(autor,tytul,kategoria,okladka,ilosc_str)
    ksiazki.append(k1)
    k1.znajdz()

k2 = Ksiazka('Adam Mickiewicz','Dziady III','Lektury','miekka',320)
k2.oddaj()

