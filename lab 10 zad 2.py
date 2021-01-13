imie = input("Podaj imię ")

nazwisko = input("Podaj nazwisko ")

numer_telefonu = input("Podaj numer telefonu ")

numer_buta = input("Podaj numer buta ")

print(imie.isalpha())

print(nazwisko.isalpha())

print(numer_telefonu.isdigit())

print(numer_buta.isdigit())

if imie.isupper() != True:
    print(imie.capitalize())

else:
    print(imie)

if nazwisko.isupper() != True:
    print(nazwisko.capitalize())
else:
    print(nazwisko)
if numer_telefonu.isdigit != True:
    numer_telefonu.replace("-",'')
else:
    print(numer_telefonu)
if numer_buta.isdigit != True:
    numer_buta.replace("-",'')
else:
    print(numer_buta)
if imie.endswith("a") == True or imie == "Nel":
    if imie != "Barnaba":
        print("jest kobitą")
    else:
        print("jest Barnabą lol")
else:
    print("Jest chłopem")