tuuma = float(input("Anna tuumat (negatiivinen luku sulkee ohjelman): "))

while tuuma >= 0:
    sentti = tuuma * 2.54
    print(f'{tuuma} tuumaa on {sentti} senttimetriä.')
    tuuma = float(input("Anna tuumat: "))

print("Ohjelma suljettu.")