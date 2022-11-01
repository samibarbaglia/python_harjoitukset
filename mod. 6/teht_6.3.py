# Kirjoita funktio, joka saa parametrinaan bensiinin määrän Yhdysvaltain
# nestegallonoina ja palauttaa paluuarvonaan vastaavan litramäärän.
# Kirjoita pääohjelma, joka kysyy gallonamäärän käyttäjältä ja muuntaa sen
# litroiksi. Muunnos on tehtävä aliohjelmaa hyödyntäen. Muuntamista jatketaan
# siihen saakka, kunnes käyttäjä syöttää negatiivisen gallonamäärän.

def convert(gallon):
    litre = gallon * 3.78541178
    return litre


gallon = float(input("Anna nestegallonat: "))
while gallon > -1:
    litre = convert(gallon)
    print(f"{gallon} nestegallonaa = {litre:.2f} litraa.")
    gallon = float(input("\nAnna nestegallonat: "))





