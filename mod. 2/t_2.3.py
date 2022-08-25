kanta = float(input("Anna suorakulmion kanta:   "))
korkeus = float(input("Anna suorakulmion korkeus: "))

# laskutoimitukset
ala = kanta * korkeus
piiri = (2 * kanta) + (2 * korkeus)

# tulostukset
print(f"Suorakulmion pinta-ala on {ala:.2f}.")
print(f"Suorakulmion piiri on {piiri:1.2f}.")