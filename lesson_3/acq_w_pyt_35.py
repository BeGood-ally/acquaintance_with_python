num = int(input("введите целое число: "))
Fib_list = []
for i in range(0, abs(num)):
    if i == 0:
        c = 0
        Fib_list.append(c)
    elif i == 1:
        c = 1
        Fib_list.append(c)
    else:
        Fib_list.append(Fib_list[i - 1] + Fib_list[i - 2])
if num < 0:
    Fib_list_rev = Fib_list[::-1]
    for j in range(0, len(Fib_list_rev) - 1):
        if j % 2 != 0:
            Fib_list_rev[j] = Fib_list_rev[j] * -1
    print(Fib_list_rev + Fib_list[1:len(Fib_list)])
else:
    print(Fib_list)
