import random
tab = []
i = 0
while i < 10:
    a = int(input('Podaj liczbe: '))
    if a > 59 or a < 0:
        continue
    tab.append(a)
    i += 1
print(tab)

for i in range(0,3):
    n = random.randrange(0,59,2)
    tab.append(a)
print(tab)

for i in range(0,3):
    n = random.randrange(0,59)
    tab.pop(a)
print(tab)

tab.insert(5,3)
tab.insert(10,33)
print(tab)