print("зададим арифметическую прогрессию")
first = int(input("введите первый член прогрессии"))
d = int(input("введите коэффициент увеличения прогрессии"))
amount = int(input("введите количество членов прогрессии"))
first_way_list = list((first + i*d) for i in range(amount))
second_way = lambda x: x*d + first
second_way_list = list(map(second_way, [i for i in range(amount)]))
print(f'{first_way_list}\n{second_way_list}')