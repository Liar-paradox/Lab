a = int(input("Podaj liczbe A:"))
b = int(input("Podaj liczbe B:"))
c = int(input("Podaj liczbe C:"))
d = int(input("Podaj liczbe D:"))
if((a == b) and (a == c) and ( a == d)):
    print("Liczby są równe")
elif((a > b) and (a > c) and (a > d)):
    print("Liczba A jest największa")
elif((b > a) and (b > c) and (b > d)):
    print("Liczba B jest największa")
elif((c > b) and (c > a) and (c > d)):
    print("Liczba C jest największa")
else:
    print("Liczba D jest największa.")