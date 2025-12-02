lista_numeros = [2, 3, -5, 4, 5, 6, 7, 8, -5, -7]


def suma_menores(lista):
    suma = 0
    for n in lista:
        if n in range(1, 1001):
            suma += n
        else:
            pass
    return suma
