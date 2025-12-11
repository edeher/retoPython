"""
Crea un generador (almacenado en la variable generador)
que sea capaz de devolver de manera indefinida múltiplos de 7,
iniciando desde el mismo 7, y que cada vez que sea llamado devuelva
el siguiente múltiplo (7, 14, 21, 28...).

"""


def mi_generador():
    numero = 0
    while True:
        numero += 1
        yield numero * 7


generador = mi_generador()
