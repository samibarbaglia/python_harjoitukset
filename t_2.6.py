import random

# kolminumeroinen, syötteet
x = random.randint(0, 9)
y = random.randint(0, 9)
z = random.randint(0, 9)

print("Kolminumeroinen numerolukon koodi: " + str(x) + str(y) + str(z))

# nelinumeroinen, syötteet
a = random.randint(1, 6)
b = random.randint(1, 6)
c = random.randint(1, 6)
d = random.randint(1, 6)

# laskutoimitukset
koodi_4 = str(a) + str(b) + str(c) + str(d)

# tulostus
input("\nNelinumeroinen numerolukon koodi: " + koodi_4)