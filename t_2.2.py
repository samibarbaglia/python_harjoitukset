import math

r = float(input("Anna ympyrän säde "))
# toinen vaihtoehto: ala = math.pi * math.pow(r, 2)
ala = math.pi * r * r

# print("Ympyrän ala " + str(ala))
print(f"Ympyrän pinta-ala on {ala:.3f}")