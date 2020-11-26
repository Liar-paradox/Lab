import random

n = random.randint(1,100)
i = 0
while i < 3:
    x = int(input('Podaj liczbe: '))
    if x > n:
        print('Podales za duza wartosc')
    if x < n:
        print("Podales za mala wartosc")
    if x == n:
        print('Gratulacje')
        break
    i += 1
if i == 3:
    print('Haha przegrales podana liczba wynosi:',n)