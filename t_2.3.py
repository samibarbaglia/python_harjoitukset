kanta = float(input("Anna suorakulmion kanta:   "))
korkeus = float(input("Anna suorakulmion korkeus: "))

# laskutoimitukset
ala = kanta * korkeus
piiri = (2 * kanta) + (2 * korkeus)

# tulostukset
print("Suorakulmion pinta-ala = " + str(ala))
print(f"Suorakulmion piiri = {piiri}")