seasons = {3:"kevät", 4:"kevät", 5:"kevät",
           6:"kesä", 7:"kesä", 8:"kesä",
           9:"syksy", 10:"syksy", 11:"syksy",
           12:"talvi", 1:"talvi", 2:"talvi"}

kk = int(input("Anna kuukausi (1-12): "))
if kk in seasons:
    print(f"{kk}. kuukausi on vuodenaikaa {seasons[kk]}.")
else:
    print("Virheellinen numero!")

# TARKISTETTU TAPA:
# seasons = ("talvi", "talvi", "kevät", "kevät", "kevät", "kesä", "kesä",
#             "kesä", "syksy", "syksy", "syksy", "talvi")
# month_num = int(input("Anna kuukauden järjestysnumero: ")

# if 0 < month_num < 13:
#   print(f"{month_num}. kuukausi kuuluu vuodenaikaan {seasons[month_num-1]}")
# else:
#   print("Virheellinen syöte!")