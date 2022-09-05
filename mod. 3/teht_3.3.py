gender = input("Sukupuolesi? (N/M) ")
gender = gender.lower()
if gender == "n":
    hg_value = int(input("Hemoglobniinisi (g/l)? "))
    if hg_value < 117:
        print("Hemoglobiiniarvo on alhainen")
    elif hg_value <= 175:
        print("Hemoglobiiniarvo normaali")
    else:
        print("Hemoglobiiniarvo on korkea")

elif gender == "m":
    hg_value = int(input("Hemoglobniinisi (g/l)? "))
    if hg_value < 134:
        print("Hemoglobiiniarvo on alhainen")
    elif hg_value <= 195:
        print("Hemoglobiiniarvo normaali")
    else:
        print("Hemoglobiiniarvo on korkea")

elif not gender == "M" or "N":
    print("Virhe")