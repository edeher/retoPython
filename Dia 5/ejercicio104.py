def suma_absolutos(*args):
    total = 0
    for arg in args:
        if arg < 0:
            total += arg + (-2 * arg)
        else:
            total += arg
    return total


print(suma_absolutos(-2, -3, 5, -5, 10))
