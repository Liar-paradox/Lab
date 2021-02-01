def THB():
    x = True
    while x:
        try:
            a = input("Z czego chcesz konwertowac (THB lub USD) ")
            liczba = int(input('Podaj ilosc: '))
            if a == 'THB':
                wynik = liczba * 0.033
                print(liczba,'THB to ',round(wynik,2),'USD')
                x = False
            elif a == 'USD':
                wynik = liczba * 29.86
                print(liczba,"USD to",round(wynik,2),'USD')
                x = False
            else:
                print('Podaj THB lub USD')
        except:
            print('Podaj liczbe')

def BTC():
    x = True
    while x:
        try:
            a = input('Z czego chcesz konwertowac (BTC lub USD) ')
            liczba = int(input('Podaj ilosc: '))
            if a == 'BTC':
                wynik = liczba * 32400
                print(f'{liczba} BTC to {wynik} USD')
                x = False
            elif a == 'USD':
                wynik = liczba * 0.000031
                print(f'{liczba} USD to {wynik} BTC')
                x = False
            else:
                print('Podaj BTC lub USD')
        except:
            print('Musi podac liczbe')

def BTN():
    x = True
    while x:
        try:
            a = input('Z czego chcesz konwertowac (BTN lub USD) ')
            liczba = int(input('Podaj ilosc: '))
            if a == 'BTN':
                wynik = liczba * 0.014
                print(f'{liczba} BTN to {wynik} USD')
                x = False
            elif a == 'USD':
                wynik = liczba * 72.81
                print(f'{liczba} USD to {wynik} BTN')
                x = False
            else:
                print('Podaj BTN lub USD')
        except:
            print('Musi podac liczbe')

def MRO():
    x = True
    while x:
        try:
            a = input('Z czego chcesz konwertowac (MRO lub USD) ')
            liczba = int(input('Podaj ilosc: '))
            if a == 'MRO':
                wynik = liczba * 0.028
                print(f'{liczba} MRO to {wynik} USD')
                x = False
            elif a == 'USD':
                wynik = liczba * 36.08
                print(f'{liczba} USD to {wynik} MRO')
                x = False
            else:
                print('Podaj MRO lub USD')
        except:
            print('Musi podac liczbe')

def ETH():
    x = True
    while x:
        try:
            a = input('Z czego chcesz konwertowac (ETH lub USD) ')
            liczba = int(input('Podaj ilosc: '))
            if a == 'ETH':
                wynik = liczba * 0.00077
                print(f'{liczba} ETH to {wynik} USD')
                x = False
            elif a == 'USD':
                wynik = liczba * 1297.85
                print(f'{liczba} USD to {wynik} ETH')
                x = False
            else:
                print('Podaj ETH lub USD')
        except:
            print('Musi podac liczbe')

print('Witaj w kantorze walut jaka walute chcesz przeliczyc ?')
menu = {}
menu['1'] = 'THB - USD'
menu['2'] = 'BTC - USD'
menu['3'] = 'BTN - USD'
menu['4'] = 'MRO - USD'
menu['5'] = 'ETH - USD'
menu['6'] = 'Wyjscie'
while True:
    options = menu.keys()
    for i in options:
        print(i,menu[i])

    wybor = input('Wybierz numer: ')
    if wybor == '1':
        THB()
        break
    elif wybor == '2':
        BTC()
        break
    elif wybor == '3':
        BTN()
        break
    elif wybor == '4':
        MRO()
        break
    elif wybor == '5':
        ETH()
        break
    elif wybor == '6':
        break
    else:
        print('Podaj wlasciwy numer')