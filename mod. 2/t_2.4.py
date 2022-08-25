# Kirjoita ohjelma, joka kysyy kolme kokonaislukua. Ohjelma tulostaa lukujen summan,
# tulon ja keskiarvon.

# Syötteet
luku_1 = int(input("Anna 1. kokonaisluku "))
luku_2 = int(input("Anna 2. kokonaisluku "))
luku_3 = int(input("Anna 3. kokonaisluku "))

# Laskutoimitukset
summa = luku_1 + luku_2 + luku_3
tulo = luku_1 * luku_2 * luku_3
keskiarvo = (summa) / 3

# tulostus
# print(summa)
# print(tulo)
# print(keskiarvo)

print("\nLukujen summa: " + str(summa) + "\nLukujen tulo: " + str(tulo) +
      "\nLukujen keskiarvo: " + str(keskiarvo))

print(f"\nLukujen summa: {summa} \nLukujen tulo: {tulo} \nLukujen keskiarvo: {keskiarvo}")