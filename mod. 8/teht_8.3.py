# Kirjoita ohjelma, joka kysyy käyttäjältä kahden lentokentän ICAO-koodit.
# Ohjelma ilmoittaa lentokenttien välisen etäisyyden kilometreinä. Laskenta
# perustuu tietokannasta haettuihin koordinaatteihin. Laske etäisyys geopy-kirjaston
# avulla: https://geopy.readthedocs.io/en/stable/. Asenna kirjasto valitsemalla
# View / Tool Windows / Python Packages. Kirjoita hakukenttään geopy ja vie asennus loppuun.
from geopy.distance import geodesic
import mysql.connector

yhteys = mysql.connector.connect(
    host='127.0.0.1',
    port= 3306,
    database='flight_game',
    user='root',
    password='p4r!i3',
    autocommit=True
    )

def haku(lentokenttä):
        sql = "SELECT latitude_deg, longitude_deg FROM airport WHERE ident ='" + lentokenttä + "'"
        kursori = yhteys.cursor()
        kursori.execute(sql)
        tulos = kursori.fetchall()
        return tulos


ICAO = input(f"Anna lentokentän ICAO-koodi: ")
haku(ICAO)

ICAO2 = input(f"Anna lentokentän ICAO-koodi: ")
haku(ICAO2)

print(f"{ICAO}, {ICAO2}")

print(f"{geodesic(haku(ICAO), haku(ICAO2)).km:0.2f} kilometriä välimatkaa.")

