import random

A = []
B = []

for x in range(100):
    a = random.randrange(0,100,2)
    A.append(a)
tup_a = tuple(A)
print('ID tupli a:',id(tup_a))

for x in range(100):
    a = random.randrange(1,100,2)
    B.append(a)
tup_b = tuple(B)
print('ID tupli b:',id(tup_b))

tup_c = tup_a + tup_b
print('Dlugosc tupli',len(tup_c),'ID tupli c:',id(tup_c))
