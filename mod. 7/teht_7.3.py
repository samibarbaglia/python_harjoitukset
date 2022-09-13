# Kirjoita ohjelma lentoasematietojen hakemiseksi ja tallentamiseksi.
# Ohjelma kysyy käyttäjältä, haluaako tämä syöttää uuden lentoaseman,
# hakea jo syötetyn lentoaseman tiedot vai lopettaa. Jos käyttäjä valitsee
# uuden lentoaseman syöttämisen, ohjelma kysyy käyttäjältä lentoaseman ICAO-koodin
# ja nimen. Jos käyttäjä valitsee haun, ohjelma kysyy ICAO-koodin ja tulostaa sitä
# vastaavan lentoaseman nimen. Jos käyttäjä haluaa lopettaa, ohjelman suoritus päättyy.
# Käyttäjä saa valita uuden toiminnon miten monta kertaa tahansa aina siihen asti,
# kunnes hän haluaa lopettaa. (ICAO-koodi on lentoaseman yksilöivä tunniste.
# Esimerkiksi Helsinki-Vantaan lentoaseman ICAO-koodi on EFHK. Löydät koodeja helposti selaimen avulla.)

asemat = {}

ehdot = print(f"1 = Syötä uusi asema \n2 = Hae asemaa \n0 = Lopeta")

while True:
    numero = int(input("\nSyötä numero: "))
    if numero == 1:
        ICAO = input("Anna lentoaseman ICAO: ")
        nimi = input("Anna lentokentän nimi: ")
        asemat[ICAO] = nimi
    elif numero == 2:
        UserICAO = input("Anna ICAO: ")
        if UserICAO in asemat:
            print(f"{UserICAO} = {asemat[UserICAO]}")
        else:
            print("Syöttämälläsi ICAO:lla ei löydy lentokenttää.")
    elif numero == 0:
        print("Suljetaan ohjelma.")
        break