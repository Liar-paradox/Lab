import random
tab = []
x = int(input('Podaj dolny zakres: '))
y = int(input('Podaj gorny zakres: '))
z = int(input('Podaj ilosc liczb: '))
i = 0
while i < z:
    a = random.randint(x,y)
    tab.append(a)
    if a in tab:
        i += 1
        continue
    i += 1
print('Tablica',tab)
tab = list(dict.fromkeys(tab))

print(tab,'Dlugosc tablicy',len(tab))