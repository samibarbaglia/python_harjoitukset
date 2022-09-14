# Kirjoita ohjelma, joka kysyy käyttäjältä lentoaseman ICAO-koodin.
# Ohjelma hakee ja tulostaa koodia vastaavan lentokentän nimen ja sen
# sijaintikunnan kurssilla käytettävästä lentokenttätietokannasta.
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
ICAO = input("Anna ICAO-koodi: ")
sql = "SELECT name, municipality FROM airport WHERE ident ='" + ICAO + "'"

# suoritetaan kysely
kursori = yhteys.cursor()
kursori.execute(sql)

# haetaan ja käsitellään tulosrivit
tulos = kursori.fetchall()
for rivi in tulos:
    print(f"{rivi[0]}, {rivi[1]}")