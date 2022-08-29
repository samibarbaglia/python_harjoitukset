# kahvin osto
# jos rahaa taskussa>=5
#    osta latte
# jos ei mutta rahaa taskussa>=3
#    osta normi kahvi
# muuten
#    lähde pois

rahaa_taskussa = int(input("\nPaljonko sinulla on rahaa? "))
maistuuko_kahvi = input("Maistuuko kahvi? ")
laten_hinta = 5
kahvin_hinta = 3
teen_hinta = 2

if rahaa_taskussa >= laten_hinta and maistuuko_kahvi == "Joo":
    print("Osta latte")
    print("Juo latte")
    rahaa_taskussa = rahaa_taskussa - laten_hinta
elif (rahaa_taskussa >= kahvin_hinta) and (maistuuko_kahvi == "Joo"):
    print("Osta tavallinen kahvi")
    rahaa_taskussa = rahaa_taskussa - kahvin_hinta

elif not (rahaa_taskussa <= teen_hinta):
    print("Otan teen")
    rahaa_taskussa = rahaa_taskussa- teen_hinta

# elif rahaa_taskussa >= teen_hinta:
    # print("Otan teen")
    # rahaa_taskussa = rahaa_taskussa - teen_hinta
else:
    print("Lähden kotiin")

if rahaa_taskussa == 0:
    print("Rahat loppu")
else:
    print(f"\nSinulla on vielä {rahaa_taskussa} euroa taskussa.")

# ikäesimerkki matskusta
ikä = int(input("Anna ikä: "))
if 15<=ikä<18:
    paino = float(input("Anna paino (kg): "))
if ikä>=18 or (ikä>=15 and paino>=55):
    print("Lääkkeen käyttö on sallittua.")