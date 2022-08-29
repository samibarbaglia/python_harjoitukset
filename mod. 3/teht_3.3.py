gender = input("Sukupuolesi? (nainen/mies) ")
# if not gender != "mies" or "nainen":
    # print("Tapahtui virhe")
    # quit()

# hg_value = int(input("Hemoglobniinisi (g/l)? "))

if gender == "nainen":
    # testataan naisen ohjearvoja vastaan
    hg_value = int(input("Hemoglobniinisi (g/l)? "))
    if hg_value < 117:
        print("Hemoglobiiniarvo on alhainen")
    elif hg_value <= 175:
        print("Hemoglobiiniarvo normaali")
    else:
        print("Hemoglobiiniarvo on korkea")

elif gender == "mies":
    # TODO: tee sama miehen arvoilla
    hg_value = int(input("Hemoglobniinisi (g/l)? "))
    if hg_value < 134:
        print("Hemoglobiiniarvo on alhainen")
    elif hg_value <= 195:
        print("Hemoglobiiniarvo normaali")
    else:
        print("Hemoglobiiniarvo on korkea")

elif not gender == "mies" or "nainen":
    print("Virhe")
    # TODO: tulosta virheilmoitus(?)