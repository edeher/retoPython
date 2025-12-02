def chequear_3_ciras(numero):
    return numero in range(100, 1000)


suma = 585 + 345
resultado = chequear_3_ciras(suma)
print(resultado)  # Debería imprimir: True

print("------------------------------------")


def chequear_33_cifras(lista):
    for n in lista:
        if n in range(100, 1000):
            return True
        else:
            pass
    return False


resultado = chequear_33_cifras([45, 678, 1234, 9])
print(resultado)  # Debería imprimir: True
print("------------------------------------")


def chequear_333_cifras(lista):
    lista3 = []
    for n in lista:
        if n in range(100, 1000):
            lista3.append(n)
        else:
            pass
    return lista3


resultado1 = chequear_333_cifras([45, 678, 1234, 9])
print(resultado1)

print("------------------------------------")


def todos_positivos(lista6):
    for n in lista6:
        if n > 0:
            pass
        else:
            return False
    return True


lista_numeros = [1, 2, 3, 4, 5, 6, -3, -5, -7]
resultado = todos_positivos(lista_numeros)
print(resultado)  # Debería imprimir: False

print("------------------------------------")


def suma_menores(lista):
    suma = 0
    for n in lista:
        if n in range(1, 1001):
            suma += n
        else:
            pass
    return suma


lista_numeros2 = [-1, 2, 3, -5, 4, 5, -7, 6, 7, 8, -5, -7]
resultado = suma_menores(lista_numeros2)
print(resultado)  # Debería imprimir: 35


print("------------------------------------")


def cantidad_pares(lista):
    cont = 0
    for n in lista:
        if n % 2 == 0:
            cont += 1
        else:
            pass
    return cont


lista_numeros = [4, 5, 67, 3, 4, 8, 10]
resultado = cantidad_pares(lista_numeros2)
print(resultado)
