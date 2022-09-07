# Muokkaa edellistä funktiota siten, että funktio saa
# parametrinaan nopan tahkojen yhteismäärän. Muokatun funktion
# avulla voit heitellä esimerkiksi 21-tahkoista roolipelinoppaa.
# Edellisestä tehtävästä poiketen nopan heittelyä jatketaan
# pääohjelmassa kunnes saadaan nopan maksimisilmäluku, joka
# kysytään käyttäjältä ohjelman suorituksen alussa.

import random
def throwDice(sides):
    diceNumber = random.randint(1, sides)
    return diceNumber

sidesLKM = int(input("Kuinka monta tahkoa? ")) # LMK = lukumäärä
while True:
    dotNumber = throwDice(sidesLKM)
    print(dotNumber)
    if dotNumber == sidesLKM:
        print("Peli loppu.")
        break
