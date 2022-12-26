import re

print("введите натуральное число больше нуля")
num = input()
itnum = re.fullmatch(r'[1-9][0-9]*', num)
if itnum:
    comp = 1
    list_of_comp = []
    for i in range(1, int(num)+1):
        comp = comp * i
        list_of_comp.append(comp)
    print(list_of_comp)
else: print("вы не ввели натуральное число больше нуля")
