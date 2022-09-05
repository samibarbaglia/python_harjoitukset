hyttiluokka = input("Syötä hyttiluokka: ")
hyttiluokka = hyttiluokka.lower()
if hyttiluokka == 'lux':
    print("KUVAUS: Parvekellinen hytti yläkannella.")
elif hyttiluokka == "a":
    print("KUVAUS: Ikkunallinen hytti autokannen yläpuolella.")
elif hyttiluokka == "b":
    print("KUVAUS: Ikkunation hytti autokannen yläpuolella.")
elif hyttiluokka == "c":
    print("KUVAUS: Ikkunaton hytti autokannen alapuolella.")
else:
    print("Virheellinen hyttiluokka")