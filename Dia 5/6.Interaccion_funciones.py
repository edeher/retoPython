from random import shuffle

# Lista inicial
palitos = ['-', '--', '---', '----']


# mesclar palitos
def mezclar(lista):
    shuffle(lista)
    return lista


print(mezclar(palitos))


# pedirle intento
def probar_suerte():
    intento = ''
    while intento not in ['1', '2', '3', '4']:
        intento = input('Elige un numero del 1 al 4: ')
    return int(intento)


# Comprobar intento

def chquear_intento(lista, intento):
    if lista[intento - 1] == '-':
        print('¡a lavar los platos!')
    else:
        print('¡Ganaste, esta vez te has salvado!')
    print(f"te ha tocado {lista[intento - 1]}")


palitos_mesclados = mezclar(palitos)
seleccion = probar_suerte()
chquear_intento(palitos_mesclados, seleccion)
