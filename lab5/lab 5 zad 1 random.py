import random
b = int(input('Podaj ilosc liczb: '))
n = 0
ile = 0
suma = 0
srednia = 0
while b > n:
    a = random.randint(-100,100)
    print(a)
    if a <= 0:
        continue
    ile += 1
    suma = int(suma) + int(a)
    srednia = suma/ile
    n += 1
print('Srednia',float(srednia))