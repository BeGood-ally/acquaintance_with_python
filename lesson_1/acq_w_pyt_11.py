print("введите номер дня недели от 1 до 7")
number = input()
weekday = [1, 2, 3, 4, 5]
holiday = [6, 7]
if int(number) in weekday:
    print("нет")
elif int(number) in holiday:
    print("да")
else:
    print("неправильный ввод числа")
