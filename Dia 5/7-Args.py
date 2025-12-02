def suma(*args):
    total = 0
    for arg in args:
        total += arg
    return total


print(suma(2, 3, 4, 5, 6, 6))

print('----------------------------------------')


def suma1(*args):
    return sum(args)


print(suma1(2, 3, 4, 5, 6, 6, 7))