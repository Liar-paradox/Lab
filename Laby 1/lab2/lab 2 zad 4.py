liczba = int(input('Podaj liczbe: '))
if liczba >= 0:
    if liczba % 2 == 0:
        print('Liczba jest dodatnia i podzielna przez 2')
    else:
        print('Liczba jest dodatnia i niepodzielna przez 2')
if liczba < 0:
    if liczba % 2 == 0:
        print('Liczba jest ujemna i podzielna przez 2')
    else:
        print('Liczba jest ujemna i niepodzielna przez 2')