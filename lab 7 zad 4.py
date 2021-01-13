tuple = ('zabka','dym','osiem','XD','hutnicza','cyrk')
n = input('Podaj slowo: ')
if n in tuple:
    print('Index slowa',tuple.index(n))
else:
    print('Nie ma tego slowa w krotce')