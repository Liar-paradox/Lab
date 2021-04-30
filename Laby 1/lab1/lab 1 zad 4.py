s = 1 #sekundy
m = s*60 #sekundy w minucie
g = m*60 #sekundy w godzinie
d = g*24 #sekundy w dniu
r = d*365.25 #sekundy w ciagu roku
z = input('Ile masz lat? ')
print(('Sekundy w minucie'),m)
print(('Sekundy w godzinie'),g)
print(('Sekundy w dniu'),d)
print(('Sekundy w ciagu roku'),r)
print(('Sekundy w ciagu zycia'),int(z) * r)