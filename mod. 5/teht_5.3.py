i = int(input("Anna kokonaisluku: "))

for n in range(2, i):
    if i % n == 0:
        print(f"{i} ei ole alkuluku.")
        break
else:
    print(f"{i} on alkuluku.")