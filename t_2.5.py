import math

leviskat = float(input("Anna leviskät: "))
naulat = float(input("\nAnna naulat: "))
luodit = float(input("\nAnna luodit: "))

# yksi vanha mitta grammoina
luoti_1 = 13.3
naula_1 = 13.3 * 32
leviska_1 = naula_1 * 20

# laskutoimituksia
lev = (leviskat * leviska_1)
nau = (naulat * naula_1)
luo = (luodit * luoti_1)

grsumma = (lev + nau + luo)
kilo = grsumma / 1000
loput = grsumma - (math.floor(kilo)) * 1000

# lopputulos

input("\nMassa nykymittoina on \n" + str(math.floor(kilo)) +
      f" kilogrammaa ja {loput:.2f} grammaa")

# testitesti
# print(summa)
# print(math.floor(kilo))
# print(loput)