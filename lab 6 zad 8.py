import random
tab = []
x = int(input('Podaj dolny zakres: '))
y = int(input('Podaj gorny zakres: '))
z = int(input('Podaj ilosc liczb: '))
i = 0

while i < z:
    a = random.randint(x,y)
    tab.append(a)
    i += 1
print(tab)
random.shuffle(tab)
print('Po pomieszaniu',tab)
tab.sort()
print('Po posortowaniu',tab)
