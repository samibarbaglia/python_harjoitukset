numbers = []
readingNumbers = True
while readingNumbers:
    strInput = input("Anna luku: ")
    if strInput == "":
        readingNumbers = False
    else:
        numbers.append(int(strInput))

numbers.sort(reverse=True)
print(numbers[:5])