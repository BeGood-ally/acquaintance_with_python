import re

print("введите число")
num = input()
itnum = re.fullmatch(r'-?([1-9][0-9]*,[0-9]+|[1-9][0-9]*|0,[0-9]+)', num)
if itnum:
    summ = 0;
    for i in num:
        if i == "," or i == "-":
            continue
        else: summ = summ + int(i)
    print(summ)
else: print("вы ввели не вещественное число")

