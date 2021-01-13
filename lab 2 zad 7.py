from math import *
a = int(input("Podaj a: "))
b = int(input("Podaj b: "))
c = int(input("Podaj c: "))

delta = b^2 - 4*a*c
print(delta)
try:
    d = sqrt(delta)
    w1 = (-b + d) / 2 * a
    w2 = (-b - d) / 2 * a
    print("Wyniki: ")
    print("x1: ", w1)
    print("x2: ", w2)
except:
    print("Delta < 0")