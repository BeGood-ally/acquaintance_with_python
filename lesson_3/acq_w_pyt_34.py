try:
    number = int(input('введите натуральное целое число: '))
    number_bin = ''
    while number > 0:
        number_bin = str(number % 2) + number_bin
        number = number // 2
    print(number_bin)
except Exception:
    print("этот символ не цифра")