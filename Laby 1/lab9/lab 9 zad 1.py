import random
teams = ['Liverpool','Chelsea','FC Barcelona','SSC Napoli','Paris Saint-Germain','KRC Genk',
        'Atlético Madryt','Włochy Atalanta BC','Francja Lille OSC','Galatasaray SK',
        'Real Madryt','Inter Mediolan','Olympique Lyon','Red Bull Salzburg',
        'Valencia CF','Bayern Monachium','Zenit Petersburg',
        'Manchester City','Borussia Dortmund','Lokomotiw Moskwa']
i = 0
A = {}
A = set(A)
B = {}
B = set(B)
C = {}
C = set(C)
D = {}
D = set(D)
while len(D) < 10 or len(C) < 10 or len(B) < 10 or len(A) < 10:
    a = random.choice(teams)
    b = random.choice(teams)
    c = random.choice(teams)
    d = random.choice(teams)
    if a not in A and len(A) < 10:
        A.add(a)
    if b not in B and len(B) < 10:
        B.add(b)
    if c not in C and len(C) < 10:
        C.add(c)
    if d not in D and len(D) < 10:
        D.add(d)

print(A,len(A))
print(B,len(B))
print(C,len(C))
print(D,len(D))
