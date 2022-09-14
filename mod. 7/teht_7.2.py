# Kirjoita ohjelma, joka kysyy käyttäjältä nimiä. Kunkin nimen
# syöttämisen jälkeen ohjelma tulostaa, joko tekstin Uusi nimi
# tai Aiemmin syötetty nimi sen mukaan, syötettiinkö nimi ensimmäistä
# kertaa. Lopuksi ohjelma luettelee syötetyt nimet yksi kerrallaan
# allekkain mielivaltaisessa järjestyksessä. Käytä joukkotietorakennetta nimien tallentamiseen.

nimet = set()

while True:
    UserInput = input("\nAnna nimi: ")
    if UserInput == "":
        break
    if UserInput in nimet:
        print("Aiemmin syötetty nimi.")
    else:
        print("Uusi nimi.")
        nimet.add(UserInput)
for p in nimet:
    print(p)
