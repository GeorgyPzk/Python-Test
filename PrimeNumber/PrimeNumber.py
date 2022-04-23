def IsPrime(n):
    d = 2
    while d * d <= n and n % d != 0:
        d += 1
    return d * d > n

fin = open('input.txt', 'r')
fout = open('output.txt', 'w')
if str(IsPrime(int(fin.read()))) == "False":
    fout.write("false")
else:
    fout.write("true")
#fout.write(str(IsPrime(int(fin.read()))))
fout.close()
