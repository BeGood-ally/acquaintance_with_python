print("введите натуральное число больше нуля")
num = input()
if num.isdecimal():
    dict = {i:  round(((1 + 1 / i) ** i), 2) for i in range(1, int(num)+1)}
    print(dict)
else: print("вы ввели символ не соответствующий запросу")
