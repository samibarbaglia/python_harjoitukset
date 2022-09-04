# Kirjoita ohjelma, joka kysyy käyttäjältä käyttäjätunnuksen ja salasanan. Jos jompikumpi
# tai molemmat ovat väärin, tunnus ja salasana kysytään uudelleen. Tätä jatketaan kunnes
# kirjautumistiedot ovat oikein tai väärät tiedot on syötetty viisi kertaa. Edellisessä
# tapauksessa tulostetaan Tervetuloa ja jälkimmäisessä Pääsy evätty.
# (Oikea käyttäjätunnus on python ja salasana rules).

correct_user = "python"
correct_password = "rules"
numberOfRounds = 5
attempts = 0

while attempts < numberOfRounds:
    attempts += 1
    user = input("Käyttäjätunnus: ")
    password =input("Salasana: ")
    if user != correct_user or password != correct_password:
        print("YRITÄ UUDELLEEN\n")
    if user == correct_user and password == correct_password:
        print("\nTervetuloa!")
        break
else:
    print("PÄÄSY EVÄTTY.")
