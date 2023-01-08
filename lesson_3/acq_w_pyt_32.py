list = [1, 5, 3, 9, 10, 3, 56, 7]
list_add = []
for i in range(0, len(list) // 2):
    list_add.append(list[i] + list[(len(list) - i) - 1])
print(list_add)