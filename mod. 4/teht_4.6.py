#import math
#import random


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