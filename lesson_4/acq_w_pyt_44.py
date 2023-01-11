import math
import random

k = int(input('введите максимальную степень многочлена: '))
polynominal = ''
while k > -1:
    l = random.randint(0,100)
    if l == 0:
        k = k - 1
        continue
    elif k == 1:
        polynominal = polynominal + str(l) + 'x'  + ' + '
        k = k - 1
    elif k == 0:
        polynominal = polynominal + str(l)
        k = k - 1
    else:
        polynominal = polynominal + str(l) + 'x^' + str(k) + ' + '
        k = k - 1

file = open('polynominal_for_44.txt','w')
file.write(polynominal)
file.close()




