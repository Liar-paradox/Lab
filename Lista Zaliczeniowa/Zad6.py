from pytemp import pytemp

def cel_far():
    a = int(input('Podaj temperature w stopniach celsjusza: '))
    fahrenheit = pytemp(a,'celsius', 'fahrenheit')
    print('temperatura w far wynosi: ',fahrenheit)
    if fahrenheit == 32:
        print('Woda zamrza')
    elif fahrenheit == 212:
        print('Woda wrze')

print(cel_far())