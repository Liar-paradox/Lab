import random
tab = []
i = 0
u = 0
for x in range(100):
    a = random.randint(0,10)
    tab.append(a)
    if a == 0:
        i += 1
    if a == 1:
        u += 1
tup = tuple(tab)
print(tup)
print('Liczba 1 powtarza sie',u)
print('Liczba 0 powtarza sie',i)
print('Liczba 2 powtarza sie',tup.count(2))

#TODO wypisac liczby parzyste i nieparzyste
krotka = ()
for x in range(100):
    krotka = krotka + (random.randint(0, 10),)
print(krotka)