# Kirjoita funktio, joka saa parametrinaan bensiinin määrän Yhdysvaltain
# nestegallonoina ja palauttaa paluuarvonaan vastaavan litramäärän.
# Kirjoita pääohjelma, joka kysyy gallonamäärän käyttäjältä ja muuntaa sen
# litroiksi. Muunnos on tehtävä aliohjelmaa hyödyntäen. Muuntamista jatketaan
# siihen saakka, kunnes käyttäjä syöttää negatiivisen gallonamäärän.

def turnToLitre(gallon):
    litre = gallon * 3.78541178
    return litre

gallon = float(input("Anna nestegallonamäärä: "))

while gallon > -1:
    litre = turnToLitre(gallon)
    print(f"{gallon} nestegallonia = {litre:.2f} litraa.")
    break





