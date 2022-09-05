userNumber = int(input("Testattava kokonaisnumero: "))
numbers = [1, 2, 3, 5, 7]

while userNumber % 1 or 2 or 3 or 5 or 7 == 0:
    print("ei")
    print("Uusiks")
if userNumber % len(numbers) != 0:
    print("joo.")
