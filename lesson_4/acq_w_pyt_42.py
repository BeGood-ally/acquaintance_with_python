number = int(input('введите натуральное целое число: '))
simple_factors = []
divided_number = number
while divided_number > 1:
    for i in range(2,abs(number)+1):
        if number%i == 0:
            simple_factors.append(i)
            divided_number = divided_number//i
            break
print(simple_factors)