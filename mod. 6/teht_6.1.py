# Kirjoita parametriton funktio, joka palauttaa paluuarvonaan satunnaisen
# nopan silmäluvun väliltä 1..6. Kirjoita pääohjelma, joka heittää noppaa
# niin kauan kunnes tulee kuutonen. Pääohjelma tulostaa kunkin heiton
# jälkeen saadun silmäluvun.

import random
def throwDice():
    diceNumber = random.randint(1,6)
    return diceNumber

while True:
    dotNumber = throwDice()
    print(dotNumber)
    if dotNumber == 6:
        print("Peli loppu.")
        break



# diceNumber = throwDice()
# for diceNumber in range(6):
#    print("Sait sen!")
