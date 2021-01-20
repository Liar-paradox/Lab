menu = {'woda':5,'cola':7,'pizza salami':25,'pizza klasyczna':23,'kotlet':22,'omlet':15}
for wartosci in menu.values():
    print(wartosci)
for klucz in menu.keys():
    print(klucz)
for klucz, wartosci in menu.items():
    print(klucz,wartosci)
del menu[max(menu, key=menu.get)]

del menu[min(menu, key=menu.get)]
print(menu)

n = input('Podaj danie: ')
b = input('Podaj cene: ')
menu[n] = b
print(menu)