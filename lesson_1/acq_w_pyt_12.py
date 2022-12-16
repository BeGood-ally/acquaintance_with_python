print("i j k  truthfulness")
for i in range(0, 2):
    for j in range(0, 2):
        for k in range(0, 2):
            print(f'{i} {j} {k}      {not (i and j and k) == (not i) or (not j) or (not k)}')
