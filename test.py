X=1
Y=3
if X==1:
    print("Hello world!")
else:
    print("x not 1")

#test = input('input a number: ')
#print(test)
def func1(X, Y):
    return X + Y
Z = func1(3,6)
print(Z) 

even_numbers = [2,4,6,8]
odd_numbers = [1,3,5,7]
all_numbers = odd_numbers + even_numbers
print(all_numbers)


mas_first = [1,2,3,5]
print(mas_first)


#def multiply(lst):
#    answer = 1
#    for i in lst:
#        answer *= i
#    return answer
#print(multiply([1, 2, 3, 4, 5]))

# перебор массива
arr = [1, 2, 3]
arr = [10*i for i in arr]
print(arr)

#цикл по массиву
munl = 10
def multmass(mas_first, munl):
    for num in mas_first:
        num = num * munl
        print(num)
multmass(mas_first, munl)
print(mas_first)

#Количество элементов в массиве
number_of_elements = len(mas_first)
print("Number of elements in the list: ", number_of_elements)