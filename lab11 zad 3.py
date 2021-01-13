import math
n = int(input('Podaj wielkosc kata w stopniach: '))
a = math.radians(n)
print(a)
b = math.sin(a)
c = math.cos(a)
d = math.tan(a)
e = math.atan(a)
print('dla kata:',round(n,3),'sin',round(b,3),'cos',round(c,3),'tan',round(d,3),'ctan',round(e,3))
#TODO warunek dla tangensa przy kacie 90 stopni