# Kirjoita ohjelma, joka kysyy käyttäjältä maakoodin (esimerkiksi FI)
# ja tulostaa kyseisessä maassa olevien lentokenttien lukumäärät tyypeittäin.
# Esimerkiksi Suomen osalta tuloksena on saatava tieto siitä, että pieniä
# lentokenttiä on 65 kappaletta, helikopterikenttiä on 15 kappaletta jne.

import mysql.connector

# yhteyden avaus
yhteys = mysql.connector.connect(
    host='127.0.0.1',
    port= 3306,
    database='flight_game',
    user='root',
    password='p4r!i3',
    autocommit=True
    )

# Määritellään kysely
maakoodi = input("Anna maakoodi: ")
sql = "SELECT type, COUNT(*) FROM airport WHERE iso_country = '" + maakoodi + "' GROUP BY type"

# suoritetaan kysely
kursori = yhteys.cursor()
kursori.execute(sql)

# haetaan ja käsitellään tulosrivit
tulos = kursori.fetchall()
for rivi in tulos:
    print(f"{rivi[0]}, {rivi[1]}")