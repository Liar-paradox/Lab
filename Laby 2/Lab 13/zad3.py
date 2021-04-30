l = []
class Smartfon:
    def __init__(self,wyswietlacz,firma,nazwa):
        self.wyswietlacz = wyswietlacz
        self.firma = firma
        self.nazwa = nazwa

    def __repr__(self):
        return 'Telefon firmy {} {} z wyswietlaczem {}'.format(self.firma,self.nazwa,self.wyswietlacz)

    def parametry(self,procesor,aparat,pamiec):
        print(f'Telefon firmy {self.firma} z wyswietlaczem {self.wyswietlacz} procesorem {procesor} aparatem {aparat} i pamiecia {pamiec}')

    def zadzwon(self,numer_tel):
        print('Telefon {} {} dzwoni do {}'.format(self.firma,self.nazwa,numer_tel))

    def dodaj(self):
        l.append(self)

samsung_s20 = Smartfon(6.2,'Samsung','S20')
samsung_s10 = Smartfon(6.1,'Samsung','S10')


samsung_s20.dodaj()
samsung_s20.parametry('Exynos990','64mpx','128')
samsung_s10.dodaj()
samsung_s10.zadzwon(444424428)

print(l)