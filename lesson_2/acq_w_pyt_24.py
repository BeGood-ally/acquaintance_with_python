print("введите натуральное число 3 или большее трех")
num = input()
if num.isdecimal():
    if int(num) > 2:
        arr = [i for i in range(-int(num), int(num)+1)]
        compl = 1
        with open('file.txt') as f:
            for line in f:
                compl = compl * arr[int(line)]
        print(compl)
    else: print("вы ввели число меньше запрашиваемого значения")
else: print("вы ввели символ либо число меньшее нуля")
