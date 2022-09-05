# Kirjoita ohjelma, joka kysyy käyttäjältä viiden kaupungin nimet yksi kerrallaan
# (käytä for-toistorakennetta nimien kysymiseen) ja tallentaa ne listarakenteeseen.
# Lopuksi ohjelma tulostaa kaupunkien nimet yksi kerrallaan allekkain samassa
# järjestyksessä kuin ne syötettiin. käytä for-toistorakennetta nimien kysymiseen
# ja for/in toistorakennetta niiden läpikäymiseen.

cities = []

# cities.insert(0, userCity)
# cities.append(userCity)

for i in range(1,6):
    userCity = input(f"Anna {i}. kaupunki: ")
    cities.append(userCity)
    i =+ 1

print("\nLista kaupungeistasi:")
for city_list in cities:
    print(city_list)
# for i in range(6):
#   print(f"{i+1}. nimi: {nimet[i]}")
# for i in range(1, len(nimet)):
#   print(f"{i}. nimi: {nimet[i-1]}")