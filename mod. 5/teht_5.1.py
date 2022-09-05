import random

diceAmount = int(input("Anna arpakuutioiden määrä numeroina: "))
dice = random.randint(1,6)
summa = 0

for i in range(diceAmount):
    dice = random.randint(1, 6)
    print(f"{i+1}. nopan numero: {dice}")
    summa = summa + dice

print(f"\nNoppien yhteissumma: {summa}")