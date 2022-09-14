
from geopy import distance

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
        sql = "SELECT latitude_deg, longitude_deg FROM airport WHERE gps_code ='" + lentokenttä + "'"
        kursori = yhteys.cursor()
        kursori.execute(sql)
        tulos = kursori.fetchall()
        return tulos


ICAO = input(f"Anna lentokentän ICAO-koodi: ")
ICAO2 = input(f"Anna lentokentän ICAO-koodi: ")
loc1 = haku(ICAO)
loc2 = haku(ICAO2)

gap = distance.distance(loc1, loc2).km

print(f"{gap:0.2f} kilometriä välimatkaa.")

