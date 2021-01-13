import webbrowser
dane = {}
admin = {'admin':'admin1'}
for x in range(6):
    log = input('Podaj login: ')
    pas = input('Podaj haslo: ')
    dane[log] = pas
    if log in admin.keys() and pas in admin.values():
        print('Zostales zalogowany jako admin')
        webbrowser.open('https://www.google.pl/')
        break
    if log in admin.keys() and pas not in admin.values():
        print('zle haslo')
    else:
        print('Nie jestes adminem')
