from random import choice


def lanzar_moneda():
    return choice(['Cara', 'Cruz'])


lista_numeros = [1, 2, 3, 4, 5]


def probar_suerte(moneda, lista):
    if moneda == 'Cara':
        print("La lista se autodestruirá")
        return []
    else:
        print("La lista fue salvada")
        return lista


probar_suerte(lanzar_moneda(), lista_numeros)