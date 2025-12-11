"""
Crea un generador (almacenado en la variable generador)
que sea capaz de devolver una secuencia infinita de números,
iniciando desde el 1, y entregando un número consecutivo
superior cada vez que sea llamada mediante next.
"""


def mi_generador():
    num = 0
    while True:
        num += 1
        yield num


generador = mi_generador()