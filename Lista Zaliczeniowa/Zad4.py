def gb():
    x = True
    while x:
        try:
            a_gb = int(input("Pojemnosc dysku w gb: "))
            b_gb = a_gb * pow(10,9)
            if a_gb >= 1:
                c_gb = b_gb / pow(1024,3)
                print("Realna pojemnosc dysku wynosi",round(c_gb,2),'GB')
                x = False
            else:
                print('Nieprawidlowa liczba')
        except:
            print('Podaj liczby')
def tb():
    y = True
    while y:
        try:
            a_tb = int(input('Pojemnosc dysku w tb: '))
            b_tb = a_tb * pow(10,12)
            if a_tb == 1:
                c_tb = b_tb / pow(1024,3)
                print('Realna pojemnosc dysku wynosi',round(c_tb,2),'TB')
                y = False
            elif a_tb >1:
                c_tb = b_tb / pow(1024,4)
                print('Realna pojemnosc dysku wynosi',round(c_tb,2),'TB')
                y = False
            else:
                print('Nieprawidlowa liczba')
        except:
            print('Podaj liczby')

print("""
Witaj w konwersji wielkosci dyskow twardych na ich realna pojemnosc
wybierz pojemnosc w GB lub w TB""")
menu = {}
menu['1'] = 'GB'
menu['2'] = 'TB'
menu['3'] = 'Wyjscie'
while True:
    options = menu.keys()
    for x in options:
        print(x,menu[x])

    wybor = input("Wybierz numer: ")
    if wybor == '1':
        gb()
        break
    elif wybor == '2':
        tb()
        break
    elif wybor == '3':
        break
    else:
        print('Podano niewlasciwa liczbe')
