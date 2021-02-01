def pracodawca(brutto):
    emerytalne = 0.0976 * brutto
    rentowe = 0.065 *brutto
    wypadkowe = 0.0167 * brutto
    fundusz = 0.0245 * brutto
    FSGP = 0.01 * brutto
    return brutto + emerytalne + rentowe + wypadkowe + fundusz + FSGP
def netto(brutto):
    emerytalne = 0.0976 * brutto
    rentowe = 0.015 * brutto
    chorobowe = 0.0245 * brutto
    podstawa_skladki = brutto - (emerytalne + rentowe + chorobowe)
    zdrowotne = podstawa_skladki * 0.09
    podstawa_opodatkowania = emerytalne + rentowe + chorobowe + zdrowotne
    kwota = brutto - podstawa_opodatkowania
    zus = podstawa_skladki * 0.0775
    zaliczka_na_PIT = kwota * 0.17 - 43.76 - zus
    if zaliczka_na_PIT < 0:
        zaliczka_na_PIT = 0

    return round(brutto - (emerytalne + rentowe + chorobowe + zdrowotne + zaliczka_na_PIT), 2)
print('Witaj Kalkulatorze pracodawcy co chcesz zrobic: ')
menu = {}
menu['1'] = 'Kalkulator'
menu['2'] = 'Wyjscie'
while True:
    options = menu.keys()
    for x in options:
        print(x,menu[x])

    wybor = input('Wybierz: ')
    if wybor == '1':
        brutto = int(input("Podaj kwotę brutto: "))
        netto = netto(brutto)
        print(f"Jako pracodawca wydasz: {pracodawca(brutto)}")
        print(f"Kwota netto dla pracownika wynosi: {netto}")
        break
    elif wybor == '2':
        break
    else:
        print('Wprowadz poprawna liczbe')