list = [1, 5, 3, 9, 10, 3, 56]
list_odd = []
summ = 0
for i in range(0, len(list), 2):
    summ += list[i]
    list_odd.append(str(list[i]))
print(f'на нечетных позициях элементы: {", ".join(list_odd)}, сумма которых равна: {summ}')
