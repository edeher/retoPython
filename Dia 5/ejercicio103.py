def suma_cuadrados(*cuadrados):
    total = 0
    for arg in cuadrados:
        total += arg**2
    return total


print(suma_cuadrados(1, 2, 3, 5))
