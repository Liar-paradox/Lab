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

menu = {}
menu['1'] = 'Kalkulator'
menu['2'] = 'Wyjscie'
while True:
    options = menu.keys()
    for x in options:
        print(x,menu[x])

    wybor = input('Podaj liczbe: ')
    if wybor == '1':
        print("Witaj w kalkulatorze placy netto/brutto")
        brutto = int(input("Kwota w brutto: "))
        netto = netto(brutto)
        print(f"Kwota netto wynosi: {netto}")
        print("Roznica miedzy kwotami brutto i netto wynosi:", round((brutto - netto), 2))
    elif wybor == '2':
        break
    else:
        print('Wybierz poprawna liczbe')