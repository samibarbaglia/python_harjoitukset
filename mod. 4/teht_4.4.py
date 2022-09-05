# Kirjoita peli, jossa tietokone arpoo kokonaisluvun väliltä 1..10.
# Kone arvuuttelee lukua pelaajalta siihen asti, kunnes tämä
# arvaa oikein. Kunkin arvauksen jälkeen ohjelma tulostaa tekstin
# Liian suuri arvaus, Liian pieni arvaus tai Oikein. Huomaa, että
#  ei saa vaihtaa lukuaan arvauskertojen välissä.

import random

arvaus = ""
numero = random.randint(1, 10)
while arvaus != numero:
    arvaus = int(input("Arvaa numero 1-10: "))
    if arvaus > numero:
        print("Liian suuri arvaus")
    elif arvaus < numero:
        print("Liian pieni arvaus")
    elif arvaus == numero:
        print(f"Oikein! Numero on {numero}.")
