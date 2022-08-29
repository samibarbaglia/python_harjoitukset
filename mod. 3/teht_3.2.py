# Kirjoita ohjelma, joka kysyy käyttäjältä laivan hyttiluokan(LUX, A, B, C) ja
# tulostaa sen sanallisen kuvauksen alla olevan luettelon mukaisesti.Tehtävässä
# on käytettävä if / elif / else -toistorakennetta.

# LUX on parvekkeellinen hytti yläkannella.
# A on ikkunallinen hytti autokannen yläpuolella.
# B on ikkunaton hytti autokannen yläpuolella.
# C on ikkunaton hytti autokannen alapuolella.
# Jos käyttäjä syöttää kelvottoman hyttiluokan, ohjelma herjaa

hyttiluokka = input("Syötä hyttiluokka: ")

if hyttiluokka == 'LUX':
    print("KUVAUS: Parvekellinen hytti yläkannella.")
elif hyttiluokka == "A":
    print("KUVAUS: Ikkunallinen hytti autokannen yläpuolella.")
elif hyttiluokka == "B":
    print("KUVAUS: Ikkunation hytti autokannen yläpuolella.")
elif hyttiluokka == "C":
    print("KUVAUS: Ikkunaton hytti autokannen alapuolella.")

else:
    print("Virheellinen hyttiluokka")