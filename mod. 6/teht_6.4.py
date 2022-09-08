# Kirjoita funktio, joka saa parametrinaan listan kokonaislukuja.
# Ohjelma palauttaa listassa olevien lukujen summan. Kirjoita testausta
# varten pääohjelma, jossa luot listan, kutsut funktiota ja tulostat sen
# palauttaman summan.

def summaa(list):
    summa = 0
    for luku in list:
        summa = summa + luku
    return summa


lista = [2, 4, 9, -4, 6, 1000]
print(summaa(lista))
