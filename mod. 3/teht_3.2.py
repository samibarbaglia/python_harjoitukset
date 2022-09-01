hyttiluokka = input("Syötä hyttiluokka: ")

if hyttiluokka == 'LUX' or hyttiluokka == 'lux' or hyttiluokka == 'Lux':
    print("KUVAUS: Parvekellinen hytti yläkannella.")
elif hyttiluokka == "A" or hyttiluokka == 'a':
    print("KUVAUS: Ikkunallinen hytti autokannen yläpuolella.")
elif hyttiluokka == "B" or hyttiluokka == 'b':
    print("KUVAUS: Ikkunation hytti autokannen yläpuolella.")
elif hyttiluokka == "C" or hyttiluokka == 'c':
    print("KUVAUS: Ikkunaton hytti autokannen alapuolella.")

else:
    print("Virheellinen hyttiluokka")