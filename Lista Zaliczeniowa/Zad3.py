def quiz():
    counter = 0
    quest = ['Najmniejsza jednostka danych służąca do odczytywania zapisanych w komputerze informacji',
             'Pamięć ROM to',
             'Czy nalezy robic przerwy podczas pracy na komputerze ?',
             'Czy funkcje w Pythonie pomagaja zorganizowac kod ?',
             'Czy po studiach informatycznych bedziesz zarabiac konkretne pieniadze?',
             'Najnowsza wersja Pythona to:',
             'Listy w Pythonie tworzone sa za pomoca: ',
             'Funkcje tworzy sie za pomoca: ',
             'Moduly w Pythonie to: ',
             'Domyslny typ danych przy funkcji input jest: ']

    ans = ['a) 1 MB b) 1 bit c) 1 bajt',
           'a) programowalna pamiec jednokrotnego zapisu b) programowalna pamiec wielokrotnego zapisu',
           'a) tak b) nie c) zalezy jak wazny jest projekt',
           'a) nie b) tak',
           'a) tak b) nie c)Jestem tu bo to moja pasja',
           'a) 3.7 b) 3.8 c) 3.9',
           'a) {} b) [] c) ()',
           'a) while b) if i else c) def',
           'a) pliki z rozszerzeniem py b) biblioteki c) pakiety',
           'a) float b) int c) string']

    good = ['b','a','a','b','a','c','b','c','a','c']

    for x in range(0,len(good)):
        print(quest[x])
        print(ans[x])
        yourans = input('Odpowiedz: ')
        if yourans == good[x]:
            counter += 1
    print('Dobre odp: ',counter)
    if counter > 8:
        print('Dostales 5')
    elif 8 <= counter > 6:
        print('Dostales 4')
    elif 6 <= counter > 4:
        print('Dostales 3')
    else:
        print('Dostales 2')

print('''
Witaj na Quizie informatycznym 
sprawdzisz tutaj swoja wiedze z zakresu informatyki i Pythona
''')
quiz()