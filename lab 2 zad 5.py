wartosc = float(input("Podaj ilość alkoholu w wydychanym powietrzu(mg/L):"))
promil = wartosc * 2.1
print("Wynik w promilach", promil, "%o")
if((promil == 0.2) or (promil < 0.2)):
    print("Jesteś trzeźwy mozesz jechać:")
else:
    print("Jesteś pijany i nie mozesz jechac")