def multiple(a, b):
    c = 1
    if b == 0:
        return c
    elif b == 1:
        return a
    else:
        return a*multiple(a, b-1)

print(multiple(3,4))