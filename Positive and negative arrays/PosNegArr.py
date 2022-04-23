import os

inputArr = []
positiveNumbers = []
negativeNumbers = []
zeronum = []

with open("input.txt", encoding="utf-8") as f:
    for line in f:
        inputArr += line.strip().split(",")

def func(inputArr):
    for num in inputArr:
        num = int(num)
        if num > 0:
            positiveNumbers.append(num)
        elif num < 0:
            negativeNumbers.append(num)
        else:
            zeronum.append(num)

func(inputArr)

#os.mkdir("Tests")
NumElementsPos = len(positiveNumbers)
x=0
foutPos = open('output1.txt', 'w')
for index in positiveNumbers:
    index = str(index)
    x=x+1
    if x < NumElementsPos:
        foutPos.write(index + ',')
    else:
        foutPos.write(index)
#foutPos.write(str(positiveNumbers))
foutPos.close()


NumElementsNeg = len(negativeNumbers)
y=0
foutNeg = open('output2.txt', 'w')
for index in negativeNumbers:
    index = str(index)
    y=y+1
    if y < NumElementsNeg:
        foutNeg.write(index + ',')
    else:
        foutNeg.write(index)
#foutPos.write(str(negativeNumbers))
foutNeg.close()

#str_a = ','.join(positiveNumbers)  # 'abc'
#print(str_a)