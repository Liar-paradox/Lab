liczba_a = int(input('Podaj Liczbe a: '))
liczba_b = int(input('Podaj liczbe b: '))
liczba_c = int(input('Podaj liczbe c: '))
if liczba_a < liczba_b:
    if liczba_b == liczba_c:
        print('Liczby b i c sa najwieksze')
    elif liczba_b > liczba_c:
        print('Liczba b jest najwieksza')
    else:
        print('Liczba c jest najwieksza')
else:
    if liczba_a == liczba_c:
        print('liczby a i c sa najwieksze')
    elif liczba_a > liczba_c:
        print('Liczba a jest najwieksza')
    else:
        print('Liczba c jest najwieksza')