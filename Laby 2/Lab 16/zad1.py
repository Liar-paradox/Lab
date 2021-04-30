import sqlite3


lista = []

conn = sqlite3.connect("kontakty.db")

conn.execute("""CREATE TABLE KONTAKTY
                (ID INT PRIMARY KEY NOT NULL,
                NAME TEXT NOT NULL,
                 NR INT NOT NULL)""")
def aktualizacja():
    cur = conn.execute('SELECT * from kontakty')
    for x in cur:
        temp = Osoba(x[0],x[1])
        lista.append(temp)

def wyszukaj(numer):
    for x in lista:
        if x.numer == numer:
            print('Podany numer znajduje sie w kontaktach')
def przegladaj():
    for x in lista:
        print(x)


class Osoba:
    def __init__(self, imie, nr):
        self.imie = imie
        self.nr = nr

    def __repr__(self):
        return "{} numer tel:{}".format(self.imie,self.nr)




conn.execute("INSERT INTO KONTAKTY(ID, NAME, NR) VALUES(1,'Adam',123321123)")
conn.execute("INSERT INTO KONTAKTY(ID, NAME, NR) VALUES(2,'Marcin',123123123)")
conn.execute("INSERT INTO KONTAKTY(ID, NAME, NR) VALUES(3,'Jan',192333444)")
conn.commit()
conn.close()
