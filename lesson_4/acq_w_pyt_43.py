rel_nums = [2, 5, 6, 2, 3, 3, 3, 3, 4, 8]
temp = []
[temp.append(x) for x in rel_nums if rel_nums.count(x) == 1]
print(temp)


