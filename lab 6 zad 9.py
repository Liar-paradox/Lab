tab = []
x = int(input('Ilosc liczb: '))
i = 0
b = 0
d = 0
while i < x:
    a = int(input('Podaj liczbe: '))
    tab.append(a)
    i += 1
tab.sort()
while b < len(tab):
    if tab[b] == tab[-1]:
        d += 1
    b += 1
print(tab)
print('Najwieksza liczba to',tab[-1],'Liczba powtorzen tej liczby',d)