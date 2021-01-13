z = int(input("podaj liczbę: "))
x = 1
tab = []
while(x<=z):
    if (z%x==0):
        tab.append(x)
    x = x+1
print(tab)