import random

list_of_books = ['h', 'e', 'l', 'l', 'o', 'f', 'r', 'i', 'e', 'n', 'd']
print("задайте количество перемещений для смешивания списка")
num = input()
print(list_of_books)
if num.isdecimal():
    for i in range(0,5):
        first = list_of_books.index(random.choice(list_of_books))
        second = random.randint(0, 10)
        temp = 0
        print(f'{first} <-> {second}')
        temp = list_of_books[first]
        list_of_books[first] = list_of_books[second]
        list_of_books[second] = temp
    print(list_of_books)

