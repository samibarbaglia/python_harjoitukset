import math

säde = float(input("Anna ympyrän säde: "))
# toinen vaihtoehto: ala = math.pi * math.pow(säde, 2)
# toinen kanssa: ala = math.pi * säde ** 2
ala = math.pi * säde * säde

# print("Ympyrän ala " + str(ala))
print(f"Ympyrän pinta-ala on {ala:.3f}")