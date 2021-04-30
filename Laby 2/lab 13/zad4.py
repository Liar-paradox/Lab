lista = []
class Student:
    def __init__(self,kierunek,imie,nazwisko,nr_tel,adres,):
        self.kierunek = kierunek
        self.imie = imie
        self.nazwisko = nazwisko
        self.nr_tel = nr_tel
        self.adres = adres

    def __repr__(self):
        return '{} {} studiuje {} nr:{} adres {}'.format(self.imie,self.nazwisko,self.kierunek,self.nr_tel,self.adres)

    def studia(self):
        print('{} {} studiuje {}'.format(self.imie,self.nazwisko,self.kierunek))

    def czas_wolny(self,zainteresowanie):
        print('{} {} w czasie wolnym zajmuje sie {}'.format(self.imie,self.nazwisko,zainteresowanie))

    def lista_studentow(self):
        lista.append(self)


s1 = Student('Informatyka','Andrzej','Kepa',444644777,'Legnicka 11')
s2 = Student('Prawo','Adrian','Kowalski',777761232,'Kwiatowa')
s1.lista_studentow()
s2.lista_studentow()
print(lista)
s1.czas_wolny('programowaniem')
s2.studia()