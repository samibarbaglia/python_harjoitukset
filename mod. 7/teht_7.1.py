seasons = {3:"kevät", 4:"kevät", 5:"kevät",
           6:"kesä", 7:"kesä", 8:"kesä",
           9:"syksy", 10:"syksy", 11:"syksy",
           12:"talvi", 1:"talvi", 2:"talvi"}

kk = int(input("Anna kuukausi (1-12): "))
if kk in seasons:
    print(f"{kk}. kuukausi on vuodenaikaa {seasons[kk]}.")