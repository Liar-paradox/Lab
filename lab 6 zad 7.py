import random
n = 1
d = 0
z = int(input('Ile razy chcesz losowac: '))
y = 0
tab = []
tab2 = []
while y < z:
    print('Losowanie',n)
    n += 1
    for x in range(0,6):
        a = int(input('Podaj liczbe: '))
        tab.append(a)
    for x in range(0,6):
        b = random.randint(1,49)
        tab2.append(b)
        if b in tab:
            d = d+1
    print('Liczba trafionych',d)
    d = 0
    y += 1
    tab = []
    tab2 = []