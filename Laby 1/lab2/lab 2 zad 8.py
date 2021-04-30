a = int(input('Podaj bok: '))
b = int(input('Podaj bok: '))
c = int(input('Podaj bok: '))

if a^2 == b^2 + c^2 or b^2 == c^2 + a^2 or c^2 == b^2 + a^2:
    print('Trojkat jest prostokatny')
else:
    print('Trojkat nie jest prostokatny')