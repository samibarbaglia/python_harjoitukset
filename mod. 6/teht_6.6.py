import math
def laske(halkaisija_cm, hinta):
    r = float(halkaisija_cm / 2)
    pinta_ala_m = (math.pi * r * r) / 1000
    arvo = hinta / pinta_ala_m
    return arvo


pizzat = []
lkm = int(input("Montako pizzaa? "))
for i in range(lkm):
    halkaisija = float(input(f"Anna {i + 1}. pizzan halkaisija (cm): "))
    hinta = float(input("Anna hinta (euroina): "))
    pizzat.append(laske(halkaisija, hinta))

# print(pizzat)

arvokkaimmanId = 0
for x in range(len(pizzat)):
    if pizzat[arvokkaimmanId] > pizzat[x]:
        arvokkaimmanId = x

print(f"Paras hinta-kokosuhde on {arvokkaimmanId + 1}. pizzassa.")