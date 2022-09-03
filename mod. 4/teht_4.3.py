userInput = input("Sano luku: ")
maxValue = minValue = int(userInput)


while userInput != "":
    userInputInt = int(userInput)
    if userInputInt < minValue:
        minValue = userInputInt
    if userInputInt > maxValue:
        maxValue = userInputInt
    userInput = input("Sano luku: ")

print(f"Pienin arvo: {minValue}. suurin arvo: {maxValue}")
