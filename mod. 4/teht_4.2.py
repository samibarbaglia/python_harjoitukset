tuuma = float(input("Anna tuumat (negatiivinen luku sulkee ohjelman): "))

while tuuma >= 0:
    sentti = tuuma * 2.54
    print(f'{tuuma} in = {sentti:.2f} cm.')
    tuuma = float(input("Anna tuumat: "))

print("Ohjelma suljettu.")
