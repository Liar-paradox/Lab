from pytemp import pytemp
n = int(input('Podaj temperature: '))
fahrenheit = pytemp(n,'celsius', 'fahrenheit')
print(fahrenheit,'f')
if fahrenheit == 212:
    print('Woda wrze')
if fahrenheit == 32:
    print('woda zamarza')
