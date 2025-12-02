lista_numeros = [1, 2, 3, 4, 5, 6, -3, -5, -7]


def todos_positivos(lista):
    for n in lista:
        if n > 0:
            pass
        else:
            return False
    return True


todos_positivos(lista_numeros)
