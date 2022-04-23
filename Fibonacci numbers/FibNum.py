def get_fib(order):
    prev = 1
    prepre = 1
    fib = 0
    if (order == 1):
        return 1

    if (order == 2):
        return 1

    num = 2
    while( order > num ):
        num = num + 1
        fib = prev + prepre
        prepre = prev
        prev = fib

    print("order: {0} value: {1}".format(order, fib))
    return fib

def save_result(res):
    fo = open('output.txt', 'w')
    fo.write(str(res) )
    fo.close()

file_name = 'input.txt'
order = 0
f = open(file_name, 'r')

for line in f:
    line = line.rstrip();
    order = int(line)
f.close()
fib_value = get_fib(order)
print("fib_value: {0}".format(fib_value))

save_result(fib_value)