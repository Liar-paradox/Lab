'''n = input('Podaj pierwsze slowo: ')
b = input('Podaj drugie slowo: ')
A = (n)
B = (b)
list1 = list(A)
list2 = list(B)
if list1 == list2:
    print('Anagram')'''

x = input("daj: ")
n = input("daj: ")
tupla1 = (x)
tupla2 = (n)
list_1 = list(tupla1)
list_2 = list(tupla2)
print(list_1)
print(list_2)
len_1 = len(list_1)
len_2 = len(list_2)
print(len_1)
print(len_2)
if len_1 != len_2:
    print("Nie są")

i = 0
counter = 0
while i < len(list_1):
    if list_1[i] in list_2:
        counter+=1
    i+=1
if counter == len_1:
    print("Anagramy")
else:
    print("Nie Anagramy")