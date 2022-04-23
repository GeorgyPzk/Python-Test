file_name = 'input.txt'

f = open(file_name, 'r')
increase_counter = 0
for line in f:
    line = line.rstrip();
    numbers = line.split(',')
    for number in enumerate( numbers ):
        cur_value = int(number[1])
        if number[0] == 0:
            prev_value = cur_value
            next
        if cur_value > prev_value:
            increase_counter = increase_counter +1

        prev_value = cur_value
f.close()
print("Increase number: {0}".format(increase_counter))

fo = open('output.txt', 'w')
fo.write(str(increase_counter) )
fo.close()