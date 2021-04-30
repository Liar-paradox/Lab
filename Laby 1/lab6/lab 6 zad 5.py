#TODO optimize
import random

tab = []
tab2 = []
a = 0
b = 0
y = 0
c = 0
x = int(input('Podaj dolny zakres: '))
z = int(input('Podaj gorny zakres: '))
i = int(input('Podaj ile liczb: '))

while y < i:
    n = random.randint(x, z)
    tab.append(n)
    y += 1
print(tab)

print('Trzeci element od konca',tab[-3])

k = int(input('Podaj ktory element usunac: '))
k = -k
tab.pop(k)
print(tab)
#TODO to powinno byc w petli
x = int(input('Podaj dolny zakres: '))
z = int(input('Podaj gorny zakres: '))
i = int(input('Podaj ile liczb: '))

while c < i:
    n = random.randint(x,z)
    tab2.append(n)
    c += 1
print('Tablica 2',tab2)
tab3 = tab + tab2
print('Tablica 3',tab3,'Dlugosc tablicy',len(tab3))
while a < len(tab3):
    z = tab3.count(tab3[a])
    print("Liczba", tab3[a] ,"powtarza się", z ,"raz/y")
    a +=z