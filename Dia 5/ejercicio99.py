lista_numeros = [4, 5, 67, 3, 4, 8, 10]


def cantidad_pares(lista):
    cont = 0
    for n in lista:
        if n % 2 == 0:
            cont += 1
        else:
            pass
    return cont
