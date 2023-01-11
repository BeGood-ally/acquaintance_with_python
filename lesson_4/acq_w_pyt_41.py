import re, math

while True:
    after_point = input('введите десятичную дробь в виде единицы с определенным количеством нулей после запятой: ')
    match = re.fullmatch(r'0.0*1', after_point)
    if match: break
    else: print('вы ввели не то, что требовалось')

print(str(math.pi)[0:len(after_point[after_point.index('.') + 1:])+2])