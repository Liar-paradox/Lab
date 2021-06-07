def kod_pl():
    x = input(int('Podaj kod pocztowy: '))
    try:
        kodzik = x.split('-')
        if len(kodzik[0]) == 2 and len(kodzik[1]) == 3:
            with open('kodypl.txt', 'w') as file:
                z = ''
                file.write(f'{z.join(kodzik)}')
    except:
        print('Podales zly kod')

def kod_us():
    x = input(int('Podaj kod pocztowy: '))
    try:
        if x == 5:
            with open('kodyus.txt', 'w') as file:
                file.write(f'{x}')
    except:
        print('Podales zly kod')