sequence = [-5, 9, 0, 3, -1, -2, 1, 4, -2, 10, 2, 0, -9, 8, 10, -9, 0, -5, -5, 7]
upper = int(input("введите верхнее значение диапазона: "))
lower = int(input("введите нижнее значение диапазона: "))
print([i for i in range(len(sequence)) if sequence[i] > lower and sequence[i] < upper])