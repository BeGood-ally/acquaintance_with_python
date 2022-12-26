print("введите натуральное число больше нуля")
num = input()
if num.isdecimal():
    dict = {i: (1 + 1 / i) ** i for i in range(1, int(num)+1)}
    print(dict)
else: print("вы ввели символ не соответствующий запросу")
