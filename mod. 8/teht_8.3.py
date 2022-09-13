# Kirjoita ohjelma, joka kysyy käyttäjältä kahden lentokentän ICAO-koodit.
# Ohjelma ilmoittaa lentokenttien välisen etäisyyden kilometreinä. Laskenta
# perustuu tietokannasta haettuihin koordinaatteihin. Laske etäisyys geopy-kirjaston
# avulla: https://geopy.readthedocs.io/en/stable/. Asenna kirjasto valitsemalla
# View / Tool Windows / Python Packages. Kirjoita hakukenttään geopy ja vie asennus loppuun.

#input("Anna 1. lentokentän ICAO-koodi: ")
#input("Anna 2. lentokentän ICAO-koodi: ")

import mysql.connector

yhteys = mysql.connector.connect(
    host='127.0.0.1',
    port= 3306,
    database='flight_game',
    user='root',
    password='p4r!i3',
    autocommit=True
    )

def Haku():
        UserIcao = input(f"Anna lentokentän ICAO-koodi: ")
        sql = "SELECT name FROM airport WHERE ident ='" + UserIcao + "'"
        kursori = yhteys.cursor()
        kursori.execute(sql)
        tulos = kursori.fetchall()
        return tulos

ICAO = Haku()
ICAO2 = Haku()

print(f"{ICAO}, {ICAO2}")

# En ymmärtänyt miten käyttää geopyä
