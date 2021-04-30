class Samochod:
    def __init__(self,marka,model,cena,przebieg,kolor):
        self.marka = marka
        self.model = model
        self.cena = cena
        self.przebieg = przebieg
        self.kolor = kolor

    def jedz_prosto(self):
        return '{} samochod marki {} jedzie prosto'.format(self.kolor, self.marka)

    def parkowanie(self):
        return  '{} samochod {} {} wykonuje manewr parkowania '.format(self.kolor, self.marka,self.model)

    def skrecanie(self, kierunek):
        if kierunek == 'lewo':
            print(f'samochod o kolorze {self.kolor} marki {self.marka} skreca w lewo')
        elif kierunek == 'prawo':
            print(f'samochod o kolorze {self.kolor} marki {self.marka} skreca w prawo')

    def wyprzedzanie(self,kolor,marka):
        return '{} {}  wyprzedza {} {}'.format(self.kolor, self.marka,kolor,marka)

samochod1 = Samochod('Ferrari','458','400000','40000','czerwone')
samochod2 = Samochod('Mazda','CX5','350000','200','czarny')

print(samochod2.parkowanie())
print(samochod1.wyprzedzanie('bialego','mercedesa'))