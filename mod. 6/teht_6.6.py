# Kirjoita funktio, joka saa parametreinaan pyöreän pizzan halkaisijan
# senttimetreinä sekä pizzan hinnan euroina. Funktio laskee ja palauttaa
# pizzan yksikköhinnan euroina per neliömetri. Pääohjelma kysyy käyttäjältä
# kahden pizzan halkaisijat ja hinnat sekä ilmoittaa, kumpi pizza antaa
# paremman vastineen rahalle (eli kummalla on alhaisempi yksikköhinta).
# Yksikköhintojen laskennassa on hyödynnettävä kirjoitettua funktiota.
import math
def laskehinta(pizzaHinnat):
        nm = 4
        for i in pizzaHalkaisijat:
            hinta = math.pi * (i/2) * (i/2)
            for luku in pizzaHinnat:
                luku = hinta / nm
        return pizzaHinnat

pizzaHalkaisijat = []
pizzaHinnat = []

for i in range(2):
    halkaisija = int(input(f"Anna {i + 1}. pizzan halkaisija (cm): "))
    pizzaHalkaisijat.append(halkaisija)

for i in range(2):
    hinta = input(f"Anna {i+1}. pizzan hinta: ")
    pizzaHinnat.append(hinta)

print(laskehinta(pizzaHinnat))

ÄÄÄÄÄÄÄ
