hyttiluokka = input("Syötä hyttiluokka: ")

if hyttiluokka == 'LUX' or 'lux' or 'Lux':
    print("KUVAUS: Parvekellinen hytti yläkannella.")
elif hyttiluokka == "A" or 'a':
    print("KUVAUS: Ikkunallinen hytti autokannen yläpuolella.")
elif hyttiluokka == "B" or 'b':
    print("KUVAUS: Ikkunation hytti autokannen yläpuolella.")
elif hyttiluokka == "C" or 'c':
    print("KUVAUS: Ikkunaton hytti autokannen alapuolella.")

else:
    print("Virheellinen hyttiluokka")