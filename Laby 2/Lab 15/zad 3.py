class Obywatel:
    def __init__(self,imie, nazwisko, ulica, nr_domu, kod_pocztowy, miejscowosc):
        self.imie = imie
        self.nazwisko = nazwisko
        self.ulica = ulica
        self.nr_domu = nr_domu
        self.kod_pocztowy = kod_pocztowy
        self.miejscowosc = miejscowosc




    def  wizytowka(self):
       print('''
       -------------------
       {} {}
       ul. {} {}
       {} {}
       -------------------
       '''.format(self.imie,self.nazwisko,self.ulica,self.nr_domu,self.kod_pocztowy,self.miejscowosc))

o1 = Obywatel('Jan','Kowalski','Rakowiecka',20,'00-001','Warszawa')
o1.wizytowka()