
numbersArr = []
inputArr2 = []
OutNumbers = []
negativeNumbers = []
zeronum = []

with open("input1.txt", encoding="utf-8") as f:
    for line in f:
        numbersArr += line.strip().split(",")

with open("input2.txt", encoding="utf-8") as f:
    for line in f:
        inputArr2 += line.strip().split(",")

def rangeFiltering(array, int1, int2):
    for num in array:
        num = int(num)
        if int(int1) < num < int(int2) :
            OutNumbers.append(num)
        else:
            negativeNumbers.append(num)

rangeFiltering(numbersArr, inputArr2[0], inputArr2[1])
