import sqlite3

conn = sqlite3.connect('pracownicy.db')

conn.execute("""CREATE TABLE PRACOWNICY
                (ID INT PRIMARY KEY NOT NULL,
                FORENAME TEXT NOT NULL,
                NAME TEXT NOT NULL,
                ADDRESS CHAR(50),
                SALARY REAL)""")
def dodawanie(idd,imie,nazwisko,adres,zarobki):
    conn.execute("INSERT INTO Pracownicy(id_pracownika, imie, nazwisko, miejscowosc, zarobki) VALUES('{}','{}','{}','{}')".format(idd,imie,nazwisko,adres,zarobki))
    conn.commit()

def usun(idd):
    conn.execute("DELETE FROM Pracownicy WHERE id_pracownika LIKE '{}'".format(idd))
    conn.commit()


def aktualizacja(imie,nazwisko,adres,zarobki,idd):
    conn.execute("UPDATE Pracownicy SET imie = '{}', nazwisko = '{}', miejscowosc = '{}', zarobki = '{}' WHERE id_pracownika = '{}'".format(imie, nazwisko, adres, zarobki, idd))
    conn.commit()


