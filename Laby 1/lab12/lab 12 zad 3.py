cal = int(input("Podaj cale: "))

cale = 2.54*cal
def cm(cale):
    finish = f'W cm: {cale/10}'
    return finish
def mm(cale):
    finish = f'W mm: {cale*10}'
    return finish
def m(cale):
    finish = f'W m: {cale}'
    return finish
def km(cale):
    finish = f'W km: {cale/1000}'
    return finish
if __name__ == "main":
    print("Wpisz w co chcesz przekształcić cale: mm,cm,m,km")
    what = input("Podaj co chcesz ode mnie: ")
    if what == 'mm':
        print(mm(cale))
    elif what == 'cm':
        print(cm(cale))
    elif what == 'km':
        print(km(cale))
    elif what == 'm':
        print(m(cale))