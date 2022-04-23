def save_result(res):
    fo = open('output.txt', 'w')
    fo.write(str(res) )
    fo.close()

file_name = 'input.txt'
f = open(file_name, 'r')
counter=0
counter_o=0
counter_a=0
for line in f:
    line = line.rstrip();
    lline = list(line)
    for el in lline:
        if el=='o' or el=='O':
            counter_o = counter_o + 1
        if el=='a' or el=='A':
            counter_a = counter_a + 1
f.close()
counter = counter_a * counter_o
print("counter: {0} counter_a: {1} counter_b: {2}".format(counter, counter_a, counter_o))

save_result(counter)