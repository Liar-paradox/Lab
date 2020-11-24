import random
b = int(input('Podaj ilosc liczb: '))
n = 0
ile = 0
suma = 0
srednia = 0
while b > n:
    a = random.uniform(-100,100)
    print(round(a,2))
    if a <= 0:
        continue
    ile += 1
    suma = float(suma) + float(a)
    srednia = float(suma/ile)
    n += 1
print('Srednia',round(srednia,2))