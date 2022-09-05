#import math
#import random

#B = (-1, -1), (1, -1), (1, 1), (-1, 1)
#n = math.pi / 4
#i = 0
#Rounds = float(input("Number of rounds: "))
#Sis = Ulkona = int(Piste)

#while i < Rounds:
    #i += 1
   # x = random.randint(-1, 1)
  #  y = random.randint(-1, 1)
   # PisteInt = int(Piste)
  #  if int(Piste) != (x^2 + y^2 < 1):
   #     PisteInt = Sis
   # if int(Piste) == (x^2 + y^2 < 1):
     #   PisteInt = Ulkona

  #  print(f"Ympyrän sisällä on {Sis} ja ulkona {Ulkona}.")


import random

inside = 0
i = 0
n = int(input("Give me the number of points: "))

while i <= n:
    x = random.uniform(-1, 1)
    y = random.uniform(-1, 1)
    if x ** 2 + y ** 2 <= 1:
        inside += 1
    i += 1

pi = 4 * inside / n

print(f"Pii is approximately: {pi}")